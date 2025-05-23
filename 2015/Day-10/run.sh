#!/bin/bash

# Array of Python versions to test
versions=("3.7" "3.8" "3.9" "3.10" "3.11" "3.12" "3.13" "3.14")

# Array of scripts to test
scripts=("loop.py" "func.py")

# Function to extract time from profiler output
get_time() {
  echo "$1" | sed -n '2p' | grep -o '[0-9]\+\.[0-9]\+ seconds' | grep -o '[0-9]\+\.[0-9]\+'
}

echo "Python Version Benchmarking"
echo "==========================="
echo

# Create a results file
results_file="python_benchmark_results.txt"
echo "Python Version Benchmarking Results" > "$results_file"
echo "===================================" >> "$results_file"
echo "$(date)" >> "$results_file"
echo >> "$results_file"

# Associative arrays to store summary results
declare -A loop_results
declare -A func_results

# Run benchmarks for each version and script
for script in "${scripts[@]}"; do
  echo "Benchmarking $script"
  echo "===============================================" >> "$results_file"
  echo "BENCHMARKING $script" >> "$results_file"
  echo "===============================================" >> "$results_file"
  echo >> "$results_file"
  
  for version in "${versions[@]}"; do
    echo "Testing Python $version with $script..."
    echo "Testing Python $version with $script..." >> "$results_file"
    
    # Run 3 times
    times=()
    for i in {1..3}; do
      echo "  Run $i..."
      
      # Run the command and capture output
      output=$(uv run --python "$version" --no-project -m cProfile "$script" 2>&1)
      exit_code=$?
      
      # Log the entire output
      echo "Run $i output:" >> "$results_file"
      echo "$output" >> "$results_file"
      echo >> "$results_file"
      
      # Check if command was successful
      if [ $exit_code -eq 0 ]; then
        # Extract time
        time_value=$(get_time "$output")
        if [ -n "$time_value" ]; then
          times+=($time_value)
          echo "  Time: $time_value seconds"
        else
          echo "  Failed to extract time from output"
          echo "  Failed to extract time from output" >> "$results_file"
        fi
      else
        echo "  Command failed with exit code $exit_code"
        echo "  Command failed with exit code $exit_code" >> "$results_file"
      fi
    done
    
    # Calculate average if we have times
    if [ ${#times[@]} -gt 0 ]; then
      sum=0
      for t in "${times[@]}"; do
        sum=$(echo "$sum + $t" | bc)
      done
      avg=$(echo "scale=4; $sum / ${#times[@]}" | bc)
      
      echo "Average time for Python $version with $script: $avg seconds"
      echo "Average time for Python $version with $script: $avg seconds" >> "$results_file"
      
      # Store in appropriate results array
      if [[ "$script" == "loop.py" ]]; then
        loop_results["$version"]=$avg
      else
        func_results["$version"]=$avg
      fi
    else
      echo "No successful runs for Python $version with $script"
      echo "No successful runs for Python $version with $script" >> "$results_file"
      
      # Store failure in appropriate results array
      if [[ "$script" == "loop.py" ]]; then
        loop_results["$version"]="Failed"
      else
        func_results["$version"]="Failed"
      fi
    fi
    
    echo >> "$results_file"
    echo
  done
  
  echo >> "$results_file"
done

# Add summary section at the end of the results file
echo "========================================" >> "$results_file"
echo "SUMMARY OF RESULTS (Average Execution Times)" >> "$results_file"
echo "========================================" >> "$results_file"
echo >> "$results_file"

echo "Python Version | loop.py Time (sec) | func.py Time (sec) | Difference (sec) | % Improvement" >> "$results_file"
echo "-------------- | ----------------- | ----------------- | ---------------- | -------------" >> "$results_file"

# Find fastest versions
fastest_loop_version=""
fastest_loop_time=999999
fastest_func_version=""
fastest_func_time=999999

for version in "${versions[@]}"; do
  loop_time="${loop_results[$version]}"
  func_time="${func_results[$version]}"
  
  # Calculate difference and improvement if both runs succeeded
  if [[ "$loop_time" != "Failed" && "$func_time" != "Failed" ]]; then
    diff=$(echo "$loop_time - $func_time" | bc)
    percent=$(echo "scale=2; ($diff / $loop_time) * 100" | bc)
    
    # Format percentage with sign
    if (( $(echo "$diff >= 0" | bc -l) )); then
      percent_str="+$percent%"
    else
      percent_str="$percent%"
    fi
    
    printf "%-14s | %-17s | %-17s | %-16s | %s\n" "Python $version" "$loop_time" "$func_time" "$diff" "$percent_str" >> "$results_file"
  else
    # At least one run failed
    if [[ "$loop_time" == "Failed" && "$func_time" == "Failed" ]]; then
      printf "%-14s | %-17s | %-17s | %-16s | %s\n" "Python $version" "Failed" "Failed" "N/A" "N/A" >> "$results_file"
    elif [[ "$loop_time" == "Failed" ]]; then
      printf "%-14s | %-17s | %-17s | %-16s | %s\n" "Python $version" "Failed" "$func_time" "N/A" "N/A" >> "$results_file"
    else
      printf "%-14s | %-17s | %-17s | %-16s | %s\n" "Python $version" "$loop_time" "Failed" "N/A" "N/A" >> "$results_file"
    fi
  fi
  
  # Update fastest versions
  if [[ "$loop_time" != "Failed" ]]; then
    if (( $(echo "$loop_time < $fastest_loop_time" | bc -l) )); then
      fastest_loop_time=$loop_time
      fastest_loop_version=$version
    fi
  fi
  
  if [[ "$func_time" != "Failed" ]]; then
    if (( $(echo "$func_time < $fastest_func_time" | bc -l) )); then
      fastest_func_time=$func_time
      fastest_func_version=$version
    fi
  fi
done

echo >> "$results_file"
echo "FASTEST VERSIONS:" >> "$results_file"
if [[ -n "$fastest_loop_version" ]]; then
  echo "Fastest for loop.py: Python $fastest_loop_version with average time $fastest_loop_time seconds" >> "$results_file"
else
  echo "Could not determine fastest version for loop.py - all runs failed" >> "$results_file"
fi

if [[ -n "$fastest_func_version" ]]; then
  echo "Fastest for func.py: Python $fastest_func_version with average time $fastest_func_time seconds" >> "$results_file"
else
  echo "Could not determine fastest version for func.py - all runs failed" >> "$results_file"
fi

echo "Benchmarking complete. Results saved to $results_file"