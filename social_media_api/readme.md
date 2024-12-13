Social Media API - Posts and Comments
Overview
This API allows users to create, view, update, and delete posts and comments within the social media platform. It supports features like pagination and filtering, providing a comprehensive solution for managing posts and comments.

Base URL
arduino
Copier le code
http://127.0.0.1:8000/api/
Authentication
All endpoints require authentication, except for listing posts. To authenticate, obtain a token via the login endpoint and include the token in the Authorization header for subsequent requests.

Example header for authentication:

makefile
Copier le code
Authorization: Token <your_token>
Posts Endpoints
1. Create a Post
Endpoint: POST /posts/
Description: Allows authenticated users to create a new post.
Request Body:
json
Copier le code
{
  "title": "My First Post",
  "content": "This is the content of the post."
}
Response:
json
Copier le code
{
  "id": 1,
  "author": 1,
  "title": "My First Post",
  "content": "This is the content of the post.",
  "created_at": "2024-12-13T00:00:00Z",
  "updated_at": "2024-12-13T00:00:00Z"
}
Permissions: Only authenticated users can create posts.
2. Get List of Posts
Endpoint: GET /posts/
Description: Lists all posts with pagination. Supports filtering by title and content.
Query Parameters:
title: Filter posts by title (case-insensitive).
content: Filter posts by content (case-insensitive).
Response:
json
Copier le code
[
  {
    "id": 1,
    "author": 1,
    "title": "My First Post",
    "content": "This is the content of the post.",
    "created_at": "2024-12-13T00:00:00Z",
    "updated_at": "2024-12-13T00:00:00Z"
  },
  {
    "id": 2,
    "author": 2,
    "title": "Another Post",
    "content": "This is another post.",
    "created_at": "2024-12-13T01:00:00Z",
    "updated_at": "2024-12-13T01:00:00Z"
  }
]
Permissions: Open to everyone (no authentication required).
3. Update a Post
Endpoint: PUT /posts/{id}/
Description: Allows the post author to update the post content.
Request Body:
json
Copier le code
{
  "title": "Updated Title",
  "content": "Updated content for the post."
}
Response:
json
Copier le code
{
  "id": 1,
  "author": 1,
  "title": "Updated Title",
  "content": "Updated content for the post.",
  "created_at": "2024-12-13T00:00:00Z",
  "updated_at": "2024-12-13T02:00:00Z"
}
Permissions: Only the post author can update the post.
4. Delete a Post
Endpoint: DELETE /posts/{id}/
Description: Allows the post author to delete their post.
Response:
json
Copier le code
{
  "detail": "Successfully deleted the post."
}
Permissions: Only the post author can delete the post.
Comments Endpoints
1. Create a Comment
Endpoint: POST /comments/
Description: Allows authenticated users to create a comment on a post.
Request Body:
json
Copier le code
{
  "post": 1,
  "content": "This is a comment on the post."
}
Response:
json
Copier le code
{
  "id": 1,
  "author": 1,
  "post": 1,
  "content": "This is a comment on the post.",
  "created_at": "2024-12-13T00:00:00Z",
  "updated_at": "2024-12-13T00:00:00Z"
}
Permissions: Only authenticated users can create comments.
2. Get List of Comments for a Post
Endpoint: GET /comments/
Description: Lists all comments. Supports filtering by post to list comments for a specific post.
Query Parameters:
post: Filter comments by post ID.
Response:
json
Copier le code
[
  {
    "id": 1,
    "author": 1,
    "post": 1,
    "content": "This is a comment on the post.",
    "created_at": "2024-12-13T00:00:00Z",
    "updated_at": "2024-12-13T00:00:00Z"
  }
]
Permissions: Open to everyone (no authentication required).
3. Update a Comment
Endpoint: PUT /comments/{id}/
Description: Allows the comment author to update their comment.
Request Body:
json
Copier le code
{
  "content": "Updated comment content."
}
Response:
json
Copier le code
{
  "id": 1,
  "author": 1,
  "post": 1,
  "content": "Updated comment content.",
  "created_at": "2024-12-13T00:00:00Z",
  "updated_at": "2024-12-13T02:00:00Z"
}
Permissions: Only the comment author can update the comment.
4. Delete a Comment
Endpoint: DELETE /comments/{id}/
Description: Allows the comment author to delete their comment.
Response:
json
Copier le code
{
  "detail": "Successfully deleted the comment."
}
Permissions: Only the comment author can delete the comment.
Pagination and Filtering
Pagination is automatically enabled for the GET /posts/ and GET /comments/ endpoints. The API will return a paginated list of results, with a default page size of 10 items per page.
Filtering is supported for posts by title and content. To filter posts, include query parameters like ?title=<keyword> or ?content=<keyword>.
Example request for filtering posts by title:

sql
Copier le code
GET /posts/?title=first
Response Status Codes
200 OK: Request was successful, and the data is returned.
201 Created: The resource was successfully created.
204 No Content: The resource was successfully deleted.
400 Bad Request: The request is malformed or missing required fields.
401 Unauthorized: Authentication is required.
403 Forbidden: The user does not have permission to perform this action.
404 Not Found: The requested resource was not found.
Example Request/Response for Creating a Post
Request:

bash
Copier le code
POST /api/posts/
Body:

json
Copier le code
{
  "title": "My First Post",
  "content": "This is the content of the post."
}
Response:

json
Copier le code
{
  "id": 1,
  "author": 1,
  "title": "My First Post",
  "content": "This is the content of the post.",
  "created_at": "2024-12-13T00:00:00Z",
  "updated_at": "2024-12-13T00:00:00Z"
}
This API documentation outlines all the necessary details for interacting with the Posts and Comments functionality in my social media platform.