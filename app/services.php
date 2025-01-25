<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $first_name = $_POST['first_name'];
    $last_name = $_POST['last_name'];
    $email = $_POST['email'];
    $password = $_POST['password'];

    // Conectar a base de datos (MySQL, por ejemplo)
    $conn = new mysqli("localhost", "root", "", "herramienta_iso50001");

    if ($conn->connect_error) {
        echo json_encode(["status" => "error", "message" => "Error al conectar a la base de datos."]);
        exit();
    }

    $stmt = $conn->prepare("INSERT INTO users (first_name, last_name, email, password) VALUES (?, ?, ?, ?)");
    $stmt->bind_param("ssss", $first_name, $last_name, $email, password_hash($password, PASSWORD_DEFAULT));
    $stmt->execute();

    echo json_encode(["status" => "success", "message" => "Usuario guardado correctamente en la base de datos."]);
    $stmt->close();
    $conn->close();
}
?>
