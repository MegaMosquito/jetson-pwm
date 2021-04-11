# jetson-pwm
Continuously change the duty cycle of a PWM on an NVIDIA Jetson nano

## Usage:

To build the container:

```
make build
```

To run the container (like a daemon, it never exits on its own, and restarts itself after reboots):

```
make run
```

To stop the container from running (and from restarting itself):

```
make stop
```

To clean up everything (remove containers and built images)

```
make clean
```

## More info

See the Makefile, Dockerfile, and python source file for more info. All are small files.

