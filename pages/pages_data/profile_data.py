from dataclasses import dataclass, field
from faker import Faker
import random

fake = Faker()


def random_gender():
    return random.choice(["male", "female", "diverse"])


def random_country_code():
    allowed_countries = ["US", "DE", "FR", "GB", "CA", "AU", "RU", "JP"]
    return random.choice(allowed_countries)


def random_phone():
    return f"+{fake.random_int(min=1, max=99)}-{fake.random_int(min=100, max=999)}-{fake.random_int(min=100, max=999)}-{fake.random_int(min=1000, max=9999)}"


def random_birthday():
    date_obj = fake.date_of_birth(minimum_age=18, maximum_age=60)
    return date_obj.strftime("%b %d, %Y").replace(" 0", " ")


def random_url_for(platform: str):
    user = fake.user_name()
    return {
        "facebook": f"https://facebook.com/{user}",
        "linkedin": f"https://linkedin.com/in/{user}",
        "instagram": f"https://instagram.com/{user}",
        "xing": f"https://xing.com/profile/{user}",
        "youtube": f"https://youtube.com/{user}",
        "vimeo": f"https://vimeo.com/{fake.random_number(digits=7)}",
        "tiktok": f"https://tiktok.com/@{user}",
        "twitter": f"https://twitter.com/{user}",
        "mastodon": f"https://mastodon.social/@{user}"
    }[platform]


@dataclass
class GeneralData:
    first_name: str = field(default_factory=fake.first_name)
    last_name: str = field(default_factory=fake.last_name)
    title: str = field(default_factory=fake.job)
    gender: str = field(default_factory=random_gender)
    street: str = field(default_factory=fake.street_address)
    zip_code: str = field(default_factory=fake.postcode)
    city: str = field(default_factory=fake.city)
    state: str = field(default_factory=fake.state)
    country: str = field(default_factory=random_country_code)
    birthday: str = field(default_factory=random_birthday)
    hide_year: bool = field(default_factory=fake.boolean)
    about: str = field(default_factory=lambda: fake.text(max_nb_chars=50))


@dataclass
class CommunicationData:
    phone_private: str = field(default_factory=random_phone)
    phone_work: str = field(default_factory=random_phone)
    mobile: str = field(default_factory=random_phone)
    fax: str = field(default_factory=random_phone)
    xmpp: str = field(default_factory=fake.email)


@dataclass
class SocialData:
    website: str = field(default_factory=fake.url)
    facebook: str = field(default_factory=lambda: random_url_for("facebook"))
    linkedin: str = field(default_factory=lambda: random_url_for("linkedin"))
    instagram: str = field(default_factory=lambda: random_url_for("instagram"))
    xing: str = field(default_factory=lambda: random_url_for("xing"))
    youtube: str = field(default_factory=lambda: random_url_for("youtube"))
    vimeo: str = field(default_factory=lambda: random_url_for("vimeo"))
    tiktok: str = field(default_factory=lambda: random_url_for("tiktok"))
    twitter: str = field(default_factory=lambda: random_url_for("twitter"))
    mastodon: str = field(default_factory=lambda: random_url_for("mastodon"))
