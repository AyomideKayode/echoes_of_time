# Echoes of Time API Documentation

## Introduction

Hi there, welcome to our API 🚀.

The "Echoes of Time" API is a virtual time capsule service where users can create time capsules, add content to them, and set them to be opened at a future date. This API supports user authentication via Firebase Auth and uses Azure Blob Storage for media content. The API is built with Flask and employs RESTful principles.

## Table of Contents

- [Base URL](#base-url)
- [Authentication](#authentication)
- [API Endpoints](#api-endpoints)
  - [Status](#status)
  - [Statistics](#statistics)
  - [Users](#users)
  - [Time Capsules](#time-capsules)
  - [Contents](#contents)
- [Models](#models)
  - [Database Storage](#database-storage)
  - [User](#user)
  - [Time Capsule](#time-capsule)
  - [Content](#content)
- [Environment Setup](#environment-setup)
- [Development Notes](#development-notes)
- [Future Enhancements](#future-enhancements)
- [Contributors](#contributors)

### Base URL

`http://localhost:5000/api/v1`

### Authentication

**API Key Authentication:**

API key authentication is required for some endpoints. The API key must be included in the request header:

```bash
X-API-KEY: <your_api_key>
```

**Firebase Authentication:**

Firebase Auth is used to secure the majority of endpoints. The Firebase ID token should be included in the request header:

```bash
Authorization: Bearer <firebase_id_token>
```

### API Endpoints

#### Status

_`GET /api/v1/status`_

- Description: Checks the status of the API.
- Headers:
  - `X-API-KEY: <your_api_key>`
- Responses:

  - `200 OK`: Returns {"status": "OK"}

  ```json
  {
    "status": "OK"
  }
  ```

#### Statistics

_`GET /api/v1/stats`_

- Description: Retrieves the statistics of the API.
- Headers:
  - `X-API-KEY: <your_api_key>`
- Responses:

  - `200 OK`: Returns the count of users, time capsules, and contents.

  ```json
  {
  "users": <number_of_users>,
  "time_capsules": <number_of_time_capsules>,
  "contents": <number_of_contents>
  }
  ```

#### Users

_`GET /api/v1/users`_

- Description: Retrieves the list of all users.
- Headers:
  - `X-API-KEY: <your_api_key>`
- Responses:

  - `200 OK`: Returns a list of users.

  ```json
  [
  {
    "id": "<user_id>",
    "username": "<username>",
    "email": "<email>",
    "last_login": "<last_login>"
  },
  ...
  ]
  ```

_`POST /api/v1/users`_

- Description: Creates a new user.
- Headers:
  - `X-API-KEY: <your_api_key>`
- Body: JSON object containing `id`, `username`, `email`, and `last_login`.
- Responses:

  - `201 Created`: Returns the created user.

  ```json
  {
    "id": "<user_id>",
    "username": "<username>",
    "email": "<email>",
    "last_login": "<last_login>"
  }
  ```

_`GET /api/v1/users/<user_id>`_

- Description: Retrieves a user by ID.
- Headers:
  - `X-API-KEY: <your_api_key>`
- Responses:

  - `200 OK`: Returns the user.

  ```json
  {
    "id": "<user_id>",
    "username": "<username>",
    "email": "<email>",
    "last_login": "<last_login>"
  }
  ```

  - `404 Not Found`: User not found.

_`DELETE /api/v1/users/<user_id>`_

- Description: Deletes a user by ID.
- Headers:
  - `X-API-KEY: <your_api_key>`
- Responses:

  - `200 OK`: User deleted.

  ```json
  {}
  ```

  - `404 Not Found`: User not found.

_`PUT /api/v1/users/<user_id>`_

- Description: Updates a user by ID.
- Headers:
  - `X-API-KEY: <your_api_key>`
- Body: JSON object containing `last_login`.

  ```json
  {
    "last_login": "<last_login>"
  }
  ```

- Responses:

  - `200 OK`: Returns the updated user.

  ```json
  {
    "id": "<user_id>",
    "username": "<username>",
    "email": "<email>",
    "last_login": "<last_login>"
  }
  ```

  - `404 Not Found`: User not found.
  - `400 Bad Request`: Invalid JSON.

_`GET /api/v1/users/<user_id>/time_capsules`_

- Description: Retrieves the list of all time capsules of a user.
- Headers:
  - Authorization: `Bearer <firebase_id_token>`
- Responses:

  - `200 OK`: Returns a list of time capsules.

  ```json
  [
  {
    "id": "<time_capsule_id>",
    "title": "<title>",
    "description": "<description>",
    "unlock_date": "<unlock_date>",
    "visibility": <visibility>,
    "status": <status>,
    "user_id": "<user_id>"
  },
  ...
  ]
  ```

  - `404 Not Found`: User not found.

#### Time Capsules

_`GET /api/v1/time_capsules`_

- Description: Retrieves the list of all public time capsules.
- Headers:
  - Authorization: `Bearer <firebase_id_token>`
- Responses:

  - `200 OK`: Returns a list of public time capsules.

  ```json
  [
  {
    "id": "<time_capsule_id>",
    "title": "<title>",
    "description": "<description>",
    "unlock_date": "<unlock_date>",
    "visibility": <visibility>,
    "status": <status>,
    "user_id": "<user_id>"
  },
  ...
  ]
  ```

_`POST /api/v1/time_capsules`_

- Description: Creates a new time capsule.
- Headers:
  - Authorization: `Bearer <firebase_id_token>`
- Body: JSON object containing `user_id`, `title`, `description`, `unlock_date`, `status`, and `visibility`.

  ```json
  {
  "user_id": "<user_id>",
  "title": "<title>",
  "description": "<description>",
  "unlock_date": "<unlock_date>",
  "status": <status>,
  "visibility": <visibility>
  }
  ```

- Responses:

  - `201 Created`: Returns the created time capsule.

  ```json
  {
  "id": "<time_capsule_id>",
  "title": "<title>",
  "description": "<description>",
  "unlock_date": "<unlock_date>",
  "visibility": <visibility>,
  "status": <status>,
  "user_id": "<user_id>"
  }
  ```

  - `400 Bad Request`: Missing or invalid data.

_`GET /api/v1/time_capsules/<time_capsule_id>`_

- Description: Retrieves a time capsule by ID.
- Headers:
  - Authorization: `Bearer <firebase_id_token>`
- Responses:

  - `200 OK`: Returns the time capsule.

  ```json
  {
  "id": "<time_capsule_id>",
  "title": "<title>",
  "description": "<description>",
  "unlock_date": "<unlock_date>",
  "visibility": <visibility>,
  "status": <status>,
  "user_id": "<user_id>"
  }
  ```

  - `404 Not Found`: Time capsule not found.

_`DELETE /api/v1/time_capsules/<time_capsule_id>`_

- Description: Deletes a time capsule by ID.
- Headers:
  - Authorization: `Bearer <firebase_id_token>`
- Responses:

  - `200 OK`: Time capsule deleted.

  ```json
  {}
  ```

  - `404 Not Found`: Time capsule not found.

_`PUT /api/v1/time_capsules/<time_capsule_id>`_

- Description: Updates a time capsule by ID.
- Headers:
  - Authorization: `Bearer <firebase_id_token>`
- Body: JSON object containing updated fields.

  ```json
  {
  "title": "<title>",
  "description": "<description>",
  "unlock_date": "<unlock_date>",
  "visibility": <visibility>,
  "status": <status>
  }
  ```

- Responses:

  - `200 OK`: Returns the updated time capsule.

  ```json
  {
  "id": "<time_capsule_id>",
  "title": "<title>",
  "description": "<description>",
  "unlock_date": "<unlock_date>",
  "visibility": <visibility>,
  "status": <status>,
  "user_id": "<user_id>"
  }
  ```

  - `404 Not Found`: Time capsule not found.
  - `400 Bad Request`: Invalid JSON.

#### Contents

_`GET /api/v1/time_capsules/<time_capsule_id>/contents`_

- Description: Retrieves the list of all contents in a time capsule.
- Headers:
  - Authorization: `Bearer <firebase_id_token>`
- Responses:

  - `200 OK`: Returns a list of contents.

  ```json
  [
  {
    "id": "<content_id>",
    "type": "<type>",
    "description": "<description>",
    "uri": "<uri>",
    "capsule_id": "<capsule_id>"
  },
  ...
  ]
  ```

  - `404 Not Found`: Time capsule not found.

_`POST /api/v1/time_capsules/<time_capsule_id>/contents`_

- Description: Creates a new content in a time capsule.
- Headers:
  - Authorization: Bearer <firebase_id_token>
- Body (Multipart Form Data):
  - `type`: `<type>` (one of image, video, audio, text)
  - `description`: `<description>`
  - `file`: File to be uploaded.
- Responses:

  - `201 Created`: Returns the created content.

  ```json
  {
    "id": "<content_id>",
    "type": "<type>",
    "description": "<description>",
    "uri": "<uri>",
    "capsule_id": "<capsule_id>"
  }
  ```

  - `400 Bad Request`: Missing or invalid data.
  - `404 Not Found`: Time capsule not found.

_`GET /api/v1/time_capsules/<time_capsule_id>/contents/<content_id>`_

- Description: Retrieves a content by ID.
- Headers:
- Authorization: `Bearer <firebase_id_token>`
- Responses:
- `200 OK`: Returns the content.

  ```json
  {
    "id": "<content_id>",
    "type": "<type>",
    "description": "<description>",
    "uri": "<uri>",
    "capsule_id": "<capsule_id>"
  }
  ```

- `404 Not Found`: Content or time capsule not found.

### Models

#### Database Storage

The db_storage module is responsible for handling all database operations.
It provides a layer of abstraction for performing CRUD (Create, Read, Update, Delete) operations on the models.

- **DBStorage Class**: Manages storage of timecapsule models in a MySQL database.

- **Attributes:**
  - `__engine`: SQLAlchemy Engine instance for database connection.
  - `__session`: SQLAlchemy Session instance for managing database transactions.

- **Methods:**
  - `__init__()`: Initializes the database connection.
  - `all(cls=None)`: Queries all objects of a given class or all classes.
  - `new(obj)`: Adds a new object to the current database session.
  - `save()`: Commits all changes of the current database session.
  - `delete(obj=None)`: Deletes an object from the current database session.
  - `reload()`: Creates all tables in the database and initializes the session.
  - `close()`: Closes the current database session.
  - `get(cls, id)`: Retrieves an object based on the class name and its ID.
  - `count(cls=None)`: Counts the number of objects in storage.

#### User

Represents a user in the system.

```py
class User(BaseModel, Base):
    __tablename__ = 'users'
    username = Column(String(150), unique=True, nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    last_login = Column(DateTime, nullable=True)
    capsules = relationship('TimeCapsule', backref='user',
                            lazy=True, cascade='all, delete-orphan')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
```

**Attributes:**

- `id (str)`: Unique identifier for the user.
- `username (str)`: Username.
- `email (str)`: Email address of the user.
- `last_login (datetime)`: Last login time.
- `time_capsules`: Relationship to the user's time capsules.

#### Time Capsule

Represents a Time Capsule for each users in the system.

```py
class TimeCapsule(BaseModel, Base):
    __tablename__ = 'time_capsules'
    user_id = Column(String(200), ForeignKey('users.id'), nullable=False)
    title = Column(String(150), nullable=False)
    description = Column(Text, nullable=True)
    unlock_date = Column(DateTime, nullable=False)
    status = Column(Boolean, default=True)
    visibility = Column(Boolean, default=True)
    contents = relationship('Content', backref='time_capsule',
                            lazy=True, cascade='all, delete-orphan')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = uuid.uuid4()
```

**Attributes:**

- `id (str)`: Unique identifier for the time capsule.
- `title (str)`: Title of the time capsule.
- `description (str)`: Description of the time capsule.
- `created_at (datetime)`: Creation date of the time capsule.
- `unlock_date (datetime)`: Date when the time capsule can be unlocked.
- `visibility (bool)`: Visibility status, whether the time capsule is public or private.
- `status (bool)`: Current status of the time capsule (e.g., "locked", "unlocked").
- `user_id (str)`: Owner's user ID. Foreign key to the user who created the time capsule.
- `contents (list)`: Relationship to the contents of the time capsule.

#### Content

Represents content within a time capsule.

```py
class Content(BaseModel, Base):
  __tablename__ = 'contents'
  capsule_id = Column(String(200), ForeignKey(
            'time_capsules.id'), nullable=False)
  type = Column(String(50), nullable=False)
  description = Column(Text, nullable=True)
  uri = Column(String(255), nullable=False)

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.id = uuid.uuid4()
```

**Attributes:**

- `id (str)`: Unique identifier for the content.
- `type (str)`: Type of content (e.g., "image", "video", "audio", "text").
- `description (text)`: Description of the content.
- `uri (str)`: URI where the content is stored.
- `capsule_id (str)`: Foreign key to the time capsule containing the content.

**Relationships:**

- **User to Time Capsules**: One-to-Many relationship. A user can have multiple time capsules.
- **Time Capsule to Contents**: One-to-Many relationship. A time capsule can contain multiple pieces of content.

### Environment Setup

- `API Key`: Set your API key in the `api/v1/views/.env` file under `API_KEY`.
- `Firebase Admin SDK`: Ensure the Firebase Admin SDK service account key is placed in the appropriate directory.

### Development Notes

- Follow RESTful principles for API design.
- Use Flask and SQLAlchemy for the backend.
- Secure endpoints with Firebase Auth.
- Validate data before processing requests.

### Future Enhancements

- Add support for additional content types.
- Implement notification system for unlock dates.
- Develop a frontend to accompany the backend, to improve our skill. _(still under development at the moment)_
- Improve error handling and logging.

### Contributors

- Abdelwadoud Makhlok ([@AbdelwadoudMakh55](https://github.com/AbdelwadoudMakh55))
- Ayomide Kayode ([@AyomideKayode](https://github.com/AyomideKayode))
