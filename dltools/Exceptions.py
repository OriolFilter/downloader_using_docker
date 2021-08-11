class UnregisteredDomain(Exception):
    """
    Raises when the domain gives isn't registred.

    In case of having this error, consider contacting the administrator and providing the link that returns error in
    order to update the list and/or add new methods
    """
    pass


class ErrorDuringContainerExecution(Exception):
    """
    For some reason the container stopped working, check the output in order to obtain more information
    """
    pass


class CannotRunTheContainer(Exception):
    """
    For some reason wasn't able to start the docker container, it might be due not being able to access the container
    (maybe due too many requests to DockerHub) or docker service isn't running
    """
    pass