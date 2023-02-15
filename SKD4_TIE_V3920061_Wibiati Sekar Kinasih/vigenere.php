<?php

// membuat fungsi enkripsi dengan parameter key dan text
function enkripsi($key, $text)
{
	
	// menginisialisasi variable
	$ki = 0; //untuk perulangan key
	$kl = strlen($key); //variabel kl digunakan untuk menampung jumlah huruf di dalam key, strlen untuk mengembalikan jumlah string dalam variabel key
	$length = strlen($text); //variabel length digunakan untuk menampung jumlah huruf di dalam text, dan akan dikembalikan oleh strlen
	
	// melakukan perulangan untuk setiap abjad
	for ($i = 0; $i < $length; $i++) //dimulai dari 0 dengan batas length (jumlah string yang dimiliki variabel text), text ini dijadikan sebuah plainteks
	{
		//jika text merupakan alphabet dengan text index ke [i] maka ini akan membaca index dari alphabet tersebut
		//jika bukan alphabet maka tidak akn dieksekusi
		if (ctype_alpha($text[$i]))
		{
			// jika text merupakan huruf kapital (semua)
			if (ctype_upper($text[$i]))
			{ 
			//variabel text [$i] untuk menampung data dari perhitungan method chr
			//method chr berfungsi untuk mengembalikan nilai ascii, kemudian mencari karakter dari nilai ascii tersebut
			//ord berfungsi utk mengubah sebuah karakter menjadi nilai ascii
			//nilai ascii dari index [$i] variabel text dikurangi nilai ascii dari A. 
			//nilai ascii dari index [$i] variabel key dikurangi nilai ascii dari A.
			//kemudian hasil dari pengurangan dari setiap variabel dijumlahkan kemudian dilanjutkan dengan perhitungan menggunakan modulo.
			//setelah mendapatkan hasil dari perhitungan tersebut maka ditambahkan dengan nilai ascii dari A karen agar hasilnya bukan merupakan nilai vertical tab
			$text[$i] = chr(((ord($text[$i]) - ord("A") + ord($key[$ki]) - ord("A")) % 26) + ord("A"));
			}
			// jika text merupakan huruf kecil (semua)
			else
			{
			//variabel text [$i] untuk menampung data dari perhitungan method chr
			//method chr berfungsi untuk mengembalikan nilai ascii, kemudian mencari karakter dari nilai ascii tersebut
			//ord berfungsi utk mengubah sebuah karakter menjadi nilai ascii
			//nilai ascii dari index [$i] variabel text dikurangi nilai ascii dari a. 
			//nilai ascii dari index [$i] variabel key dikurangi nilai ascii dari a.
			//kemudian hasil dari pengurangan dari setiap variabel dijumlahkan kemudian dilanjutkan dengan perhitungan menggunakan modulo.
			//setelah mendapatkan hasil dari perhitungan tersebut maka ditambahkan dengan nilai ascii dari a karen agar hasilnya bukan merupakan nilai vertical tab
				$text[$i] = chr(((ord($text[$i]) - ord("a") + ord($key[$ki]) - ord("a")) % 26) + ord("a"));
			}
			
			//perulangan pada key
			$ki++;
			//jika ki lebih besar dari kl maka akan mulai lagi dari 0 dan akan berlanjut hingga plainteksnya berhenti dari perulangan
			if ($ki >= $kl)
			{
				$ki = 0;
			}
		}
	}
	// mengembalikan nilai text
	return $text;
}

// membuat fungsi dekripsi
function dekripsi($key, $text)
{
	// inisialisasi variable
	$ki = 0;  //untuk perulangan key
	$kl = strlen($key); //variabel kl digunakan untuk menampung jumlah huruf di dalam key, strlen untuk mengembalikan jumlah string dalam variabel key
	$length = strlen($text); //variabel length digunakan untuk menampung jumlah huruf di dalam text, dan akan dikembalikan oleh strlen
	
	// melakukan perulangan untuk setiap abjad
	for ($i = 0; $i < $length; $i++) //dimulai dari 0 dengan batas length (jumlah string yang dimiliki variabel text), text ini dijadikan sebuah plainteks
	{
		//jika text merupakan alphabet dengan text index ke [i] maka ini akan membaca index dari alphabet tersebut
		//jika bukan alphabet maka tidak akn dieksekusi
		if (ctype_alpha($text[$i]))
		{
			// jika text merupakan huruf kapital (semua)
			if (ctype_upper($text[$i]))
			{
			//variabel x untuk menampung data dari proses perhitungan
			//ord berfungsi utk mengubah sebuah karakter menjadi nilai ascii
			//nilai ascii dari index [$i] variabel text dikurangi nilai ascii dari A. 
			//nilai ascii dari index [$i] variabel key dikurangi nilai ascii dari A.
			//kemudian hasil dari pengurangan dari setiap variabel dijumlahkan kemudian dilanjutkan dengan perhitungan menggunakan modulo.
			//menggunakan variabel x karena text yang akan didekripsi merupakan pengurangan yang rentan menemui bilangan negatif sehingga mengalami perulangan mundur
			$x = ((ord($text[$i]) - ord("A")) - (ord($key[$ki]) - ord("A")) % 26);

			//jika x kurang dari 0, maka x ditambahkan dengan 26 karena merupakan modulo atau jumlah alphabet yang digunakan A-Z 
				if ($x < 0)
				{
					$x += 26;
				}
				//x ditambahkan dengan nilai ascii dari A.
				$x = $x + ord("A");
				
				//nilai text index i didefinisikan dengan method chr yang mana ini akan mengembalikan nilai string dari ascii. 
				$text[$i] = chr($x);
			}
			
			// jika text merupakan huruf kecil (semua)
			else
			{
			//variabel x untuk menampung data dari proses perhitungan
			//ord berfungsi utk mengubah sebuah karakter menjadi nilai ascii
			//nilai ascii dari index [$i] variabel text dikurangi nilai ascii dari a. 
			//nilai ascii dari index [$i] variabel key dikurangi nilai ascii dari a.
			//kemudian hasil dari pengurangan dari setiap variabel dijumlahkan kemudian dilanjutkan dengan perhitungan menggunakan modulo.
			//menggunakan variabel x karena text yang akan didekripsi merupakan pengurangan yang rentan menemui bilangan negatif sehingga mengalami perulangan mundur
				$x = ((ord($text[$i]) - ord("a")) - (ord($key[$ki]) - ord("a")) % 26);
			//jika x kurang dari 0, maka x ditambahkan dengan 26 karena merupakan modulo atau jumlah alphabet yang digunakan a-z
				if ($x < 0)
				{
					$x += 26;
				}
				//x ditambahkan dengan nilai ascii dari a.
				$x = $x + ord("a");
				//nilai text index i didefinisikan dengan method chr yang mana ini akan mengembalikan nilai string dari ascii. 
				$text[$i] = chr($x);
			}
			//perulangan pada key
			$ki++;
			//jika ki lebih besar dari kl maka akan mulai lagi dari 0 dan akan berlanjut hingga plainteksnya berhenti dari perulangan
			if ($ki >= $kl)
			{
				$ki = 0;
			}
		}
	}
	
	// mengembalikan nilai text
	return $text;
}

?>