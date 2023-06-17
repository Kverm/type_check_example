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

    # Pyright now does care when this method is commented out!
    # It can directly compare the structure of the class with the protocol class.
    def post_message(self, message: str) -> None:
        print(f"{self.type} channel: {message}")


@dataclass
class Post:
    message: str
    timestamp: int


def process_schedule(posts: list[Post], channel: SocialChannel) -> None:
    for post in posts:
        if post.timestamp <= time():
            channel.post_message(post.message)


def main() -> None:
    posts = [
        Post(
            "Grandma's carrot cake is available again (limited quantities!)!",
            1568123400,
        ),
        Post("Get your carrot cake now, the promotion ends today!", 1568133400),
    ]
    # Mypy can infer that TwitterChannel follows the structure of the SocialChannel
    # protocol. No errors are raised.
    channel = TwitterChannel(100)
    process_schedule(posts, channel)


if __name__ == "__main__":
    main()
