<?php


#    }

// Start of another method

# check for submission
// If submission is valid, make variables from html names in document
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $FirstName = $_POST["FirstName"];
    $LastName = $_POST['LastName'];
    $email = $_POST['email'];
    $pwd=$_POST['pwd'];
    $pwd=md5($pwd);

    try {
        //Calls connection to database
        require_once "connect.php";
        //two methods name parameters and not name parameters, if you name the values, it requires binding
        $query = "INSERT INTO people(firstName, lastName, email, pwd)
        VALUES (:FirstName, :LastName, :email, :pwd)";

        $stmt = $conn->prepare($query);

        $stmt->bindParam(":FirstName", $FirstName);
        $stmt->bindParam(":LastName", $LastName);
        $stmt->bindParam(":email", $email);
        $stmt->bindParam(":pwd", $pwd);

        $stmt->execute();

        $conn = null;
        $stmt = null;

        header("Location: ../oysters.php");

        die();
    } catch (Exception $e) {
        die("Connection failed" . $e->getMessage());
    }
}
# sends user back to homepafge if they didnt access it correctly
else {
    header("Location: ../oysters.php");
}
