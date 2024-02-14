<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>vid_index</title>
</head>
<body>
    <div>
        <a href="/">home</a>
        <a href="/bid_gehitu">bideojokua gehitu</a>

    </div>
    <table border="1">
        <tr>
            <th>id</th>
            <th>bid_izena</th>
            <th>bid_deskripzioa</th>
            <th>x</th>
            <th>=</th>
        </tr>
        @foreach ($bideojokua as $bideojokua)
            <tr>
                <td>{{ $bideojokua->id }}</td>
                <td>{{ $bideojokua->bid_izena }}</td>
                <td>{{ $bideojokua->bid_deskripzioa }}</td>
                <td><a href="/delete/{{ $bideojokua->id }}" style="color:red;">x</a></td>
                <td><a href="/edit/{{ $bideojokua->id }}" style="color:orange;">=</a></td>
            </tr>
        @endforeach
    </table>
</body>
</html>