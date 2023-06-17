from dataclasses import dataclass, field
from time import time
from typing import Protocol, runtime_checkable


class SocialChannel(Protocol):
    def post_message(self, message: str) -> None:
        ...


@dataclass
class YoutubeChannel:
    type: str = field(init=False, default="Youtube")
    followers: int

    def post_message(self, message: str) -> None:
        print(f"{self.type} channel: {message}")


@dataclass
class FacebookChannel:
    type: str = field(init=False, default="Facebook")
    followers: int

    def post_message(self, message: str) -> None:
        print(f"{self.type} channel: {message}")


@dataclass
class TwitterChannel:
    type: str = field(init=False, default="Twitter")
    followers: int

    # Pyright doesn't care when commenting out this method, even though the class
    # is used in process_schedule() and should adhere to the protocol.
    def post_message(self, message: str) -> None:
        print(f"{self.type} channel: {message}")


@dataclass
class Post:
    message: str
    timestamp: int


def process_schedule(posts: list[Post], channels: list[SocialChannel]) -> None:
    for post in posts:
        if post.timestamp <= time():
            for channel in channels:
                channel.post_message(post.message)


def main() -> None:
    posts = [
        Post(
            "Grandma's carrot cake is available again (limited quantities!)!",
            1568123400,
        ),
        Post("Get your carrot cake now, the promotion ends today!", 1568133400),
    ]
    # Mypy throws the following error:
    # exercise_1_abstract_protocol.py:65: error: Argument 2 to "process_schedule" has
    # incompatible type "List[object]"; expected "List[SocialChannel]"  [arg-type]
    #
    # When providing the explicit type hint `list[SocialChannel])` to channels,
    # the error is solved.
    channels = [
        YoutubeChannel(100),
        FacebookChannel(100),
        TwitterChannel(100),
    ]
    process_schedule(posts, channels)


if __name__ == "__main__":
    main()
