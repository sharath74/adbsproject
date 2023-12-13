<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Movie and Actor Database</title>
</head>
<body>
    <h2>Movies</h2>
    <ul>
        % for movie in movies:
            <li>{{ movie[1] }} <a href="/edit/movie/{{ movie[0] }}">Edit</a> <a href="/delete/movie/{{ movie[0] }}">Delete</a></li>
        % end
    </ul>

    <h2>Actors</h2>
    <ul>
        % for actor in actors:
            <li>{{ actor[1] }} <a href="/edit/actor/{{ actor[0] }}">Edit</a> <a href="/delete/actor/{{ actor[0] }}">Delete</a></li>
        % end
    </ul>

    <a href="/add">Add New</a>
</body>
</html>
