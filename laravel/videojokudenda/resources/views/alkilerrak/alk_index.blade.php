<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>alk_index</title>
</head>
<body>
    <div>
        <a href="/">home</a>
        <a href="/alk_gehitu">alkilerra gehitu</a>
    </div>
    <table border="1">
        <tr>
            <th>id</th>
            <th>bez_izena</th>
            <th>bid_izena</th>
            <th>hasiera_data</th>
            <th>amaiera_data</th>
            <th>x</th>
        </tr>
        @foreach ($alkilerra as $alkilerra)
            <tr>
                <td>{{ $alkilerra->id }}</td>
                <td>{{ $alkilerra->bezeroa->izena }}</td>
                <td>{{ $alkilerra->bideojokua->bid_izena }}</td>
                <td>{{ $alkilerra-> hasiera_data}}</td>
                <td>{{ $alkilerra-> amaiera_data}}</td>
                <td><a href="/alk_delete/{{ $alkilerra->id }}" style="color:red;">x</a></td>
            </tr>
        @endforeach
    </table>
</body>
</html>