class Member:
    def __init__(self, name, member_id, email=None):
        self.name = name
        self.member_id = member_id   # e.g., "M001"
        self.email = email

    def __repr__(self):
        email_str = f" <{self.email}>" if self.email else ""
        return f"{self.name} (ID: {self.member_id}){email_str}"

    def to_dict(self):
        return {
            "name": self.name,
            "member_id": self.member_id,
            "email": self.email
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            member_id=data["member_id"],
            email=data.get("email")
        )