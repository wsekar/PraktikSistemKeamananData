<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <title>Sistem Keamanan Data</title>
</head>

<body>
    <div class="container">
        <div class="card card-outline card-primary">
            <div class="card-header text-center">
                <h4><b>SISTEM KEAMANAN DATA</b></h4>
            </div>
            <div class="card-body">
                <?php
                // inisialisasi variabel 
                $key = "";
                $text = "";
                $notif = "";

                // memanggil fungsi enkripsi dan dekripsi dari file vigenere.php
                // mendeklarasikan fungsi enkripsi dan dekripsi
                require_once('vigenere.php');
                $key = $_POST['key'];
                $text = $_POST['text'];

                //jika menekan tombol enkripsi
                if (isset($_POST['enkripsi'])) {
                    $text = enkripsi($key, $text);
                    $notif = "Text berhasil di enkripsi!";
                }

                // jika menekan tombol dekripsi
                if (isset($_POST['dekripsi'])) {
                    $text = dekripsi($key, $text);
                    $notif = "Text berhasil di dekripsi!";
                }
                ?>

                <!-- Form  -->
                <form name="skd" method="post">
                    <!-- Form input key -->
                    <div class="form-group">
                        <label for="key">Key</label>
                        <input type="text" name="key" class="form-control" placeholder="Input Key" min=1 max=30>
                    </div>
                    <!-- Form input text -->
                    <div class="form-group">
                    <label for="key">Text</label>
                        <textarea name="text" class="form-control" placeholder="Input Text" rows="5"></textarea>
                    </div>
                    <div class="box-footer">
                        <table class="table table-stripped">
                            <tr>
                                <!-- button enkripsi dan dekripsi -->
                                <td><input class="btn btn-primary" type="submit" name="enkripsi" value="Enkripsi" style="width: 100%"></td>
                                <td><input class="btn btn-primary" type="submit" name="dekripsi" value="Dekripsi" style="width: 100%"></td>
                            </tr>
                        </table>
                    </div>
                </form>
            </div>

            <!-- Hasil enkripsi/dekripsi -->
            <div class="card-header text-center">
                <h4><b><?php echo $notif; ?></b></h4>
            </div>
            <div class="card-body">
                <table>
                    <!-- Menampilkan hasil output dari enkripsi/dekripsi -->
                    <tr>
                        <td> Output yang dihasilkan : </td>
                        <td><b>
                                <?php if (isset($_POST['enkripsi'])) { //jika tombol enkripsi yang ditekan
                                    echo $text; //menampilkan output
                                }
                                if (isset($_POST['dekripsi'])) { //jika tombol dekripsi yang ditekan
                                    echo $text; //menampilkan output
                                } ?></b></td>
                    </tr>
                    <tr>
                        <!-- menampilkan text yang dimasukkan -->
                        <td>Text yang dimasukkan : </td>
                        <td><b>
                                <?php if (isset($_POST['enkripsi'])) { //jika tombol enkripsi yang ditekan
                                   echo $_POST['text']; //menampilkan input
                                }
                                if (isset($_POST['dekripsi'])) { //jika tombol dekripsi yang ditekan
                                    echo $_POST['text']; //menampilkan input
                                } ?></b></td>
                    </tr>
                    <tr>
                        <td>Key : </td>
                        <td><b><?php if (isset($_POST['enkripsi'])) { //jika tombol enkripsi yang ditekan
                                    echo $_POST['key']; //memanggil dan menampilkan key atau kunci geser
                                }
                                if (isset($_POST['dekripsi'])) { //jika tombol dekripsi yang ditekan
                                    echo $_POST['key']; //memanggil dan menampilkan key atau kunci geser
                                } ?></b></td>
                    </tr>
                </table>
            </div>
        </div>
    </div>
    </form>

</body>

</html>
<style>
    body {
        background-color: #A7BBC7;
    }

    .container {
        width: 45%;
        margin: 45px auto;
    }
</style>