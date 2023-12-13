<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add New</title>
</head>
<body>
    <h2>Add New</h2>
    <form action="/add" method="post">
        <label for="entity_type">Entity Type:</label>
        <select name="entity_type" id="entity_type">
            <option value="movie">Movie</option>
            <option value="actor">Actor</option>
        </select><br>
        <label for="name">Name:</label>
        <input type="text" name="name" id="name" required><br>
        <input type="submit" value="Add">
    </form>
    <a href="/">Back to Home</a>
</body>
</html>

