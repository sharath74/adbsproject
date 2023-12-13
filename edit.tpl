<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit</title>
</head>
<body>
    <h2>Edit {{ entity_type.capitalize() }}</h2>
    <form action="/edit/{{ entity_type }}/{{ entity[0] }}" method="post">
        <label for="name">Name:</label>
        <input type="text" name="name" id="name" value="{{ entity[1] }}" required><br>
        <input type="submit" value="Update">
    </form>
    <a href="/">Back to Home</a>
</body>
</html>
