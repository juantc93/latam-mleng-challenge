#!/bin/bash
wrk  -d45s http://127.0.0.1:80/predict -s stress_config.lua | tee stress-test-results.txt