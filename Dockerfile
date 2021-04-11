# Container that spins the PWM pin up and down forever
# Tested on NVIDIA Jetson nano 2GB. Expected to work on other Jetsons.

FROM ubuntu:20.04
WORKDIR /

# Install python basics
RUN apt update && apt install -y \
  python3 python3-dev python3-pip

# Install the python GPIO library for Jetson (used for PWM)
RUN pip3 install Jetson.GPIO

# Copy over the daemon code
COPY jetson-pwm.py /

# Run the daemon
CMD python3 /jetson-pwm.py

