import threading

def throttle(min_period, max_calls=2):
    """
        Decorator that enforces throttling policy.
        Will not call let a method be called more than max_calls, unless
        min_period has elapsed.
    """

    def _throttle(protected_function):
        semaphore = threading.BoundedSemaphore(max_calls)

        # Ownership of this lock gives the right to call the throttled method
        # immediately.
        # Release doesn't guarantee the method has completed, but merely that
        # it was initiated more than a min_period ago.

        def __throttle(self, *args, **kwargs):
            semaphore.acquire()  # May be blocking!

            def __timed_release():
                semaphore.release()

            # Spawn a new thread to unlock once a suitable period has elapsed.
            # The extra millisecond is to allow for clock differences and other
            # noise.

            threading.Timer(min_period + 0.001,
                            __timed_release).start()
            return protected_function(self, *args, **kwargs)

        return __throttle

    return _throttle