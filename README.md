<!DOCTYPE html>
<html>
<head>
	
</head>
<body>
	<h1>Management System</h1>
	<nav>
		<ul>
			<li><a href="#">Home</a></li>
			<li><a href="#">Students</a></li>
			<li><a href="#">Teachers</a></li>
			<li><a href="#">Classes</a></li>
			<li><a href="#">Reports</a></li>
		</ul>
	</nav>
	<main>
		<h2>Student Management</h2>
		<form action="" method="post">
			<label for="name">Name:</label>
			<input type="text" id="name" name="name">
			<label for="age">Age:</label>
			<input type="number" id="age" name="age">
			<label for="grade">Grade:</label>
			<input type="text" id="grade" name="grade">
			<button type="submit">Add Student</button>
		</form>
		<table>
			<thead>
				<tr>
					<th>Name</th>
					<th>Age</th>
					<th>Grade</th>
					<th>Action</th>
				</tr>
			</thead>
			<tbody>
				<tr>
					<td>John Smith</td>
					<td>17</td>
					<td>11th</td>
					<td>
						<button>Edit</button>
						<button>Delete</button>
					</td>
				</tr>
				<tr>
					<td>Jane Doe</td>
					<td>16</td>
					<td>10th</td>
					<td>
						<button>Edit</button>
						<button>Delete</button>
					</td>
				</tr>
			</tbody>
		</table>
	</main>
	<footer>
		<p>&copy; 2023 Management System</p>
	</footer>
</body>
</html>
