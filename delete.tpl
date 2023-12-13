<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Delete</title>
</head>
<body>
    <h2>Confirm Deletion</h2>
    <p>Are you sure you want to delete this {{ entity_type }}?</p>
    <p>Name: {{ entity[1] }}</p>
    <form action="/delete/{{ entity_type }}/{{ entity[0] }}" method="post">
        <input type="submit" value="Delete">
    </form>
    <a href="/">Cancel</a>
</body>
</html>
