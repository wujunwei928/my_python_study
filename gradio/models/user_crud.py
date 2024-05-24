from .database_setup import User, session


def create_user(name, age):
    new_user = User(name=name, age=age)
    session.add(new_user)
    session.commit()
    return f"User {name} added."


def read_users():
    users = session.query(User).all()
    return [(user.id, user.name, user.age) for user in users]


def update_user(user_id, name, age):
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        user.name = name
        user.age = age
        session.commit()
        return f"User {user_id} updated."
    return f"User {user_id} not found."


def delete_user(user_id):
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        session.delete(user)
        session.commit()
        return f"User {user_id} deleted."
    return f"User {user_id} not found."
