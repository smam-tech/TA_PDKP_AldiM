import wpf
import random
import array

from System.Windows import Application, Window, MessageBox

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'WpfApplication1.xaml')
    

    def button_Click(self, sender, e):
        a = self.textboxEmail.Text.ToString()
        b = self.textboxID.Text.ToString()
        c = self.textboxCoupon.Text.ToString()
        d = self.textboxQTY.Text.ToString()


        if (a == "" or b == "" or d == "" or self.ComboBoxD.Text == "" or 
            (self.h10k.IsChecked == False and self.h20k.IsChecked == False and self.h50k.IsChecked == False and self.h100k.IsChecked == False and self.h250k.IsChecked == False and self.h500k.IsChecked == False and self.h1jt.IsChecked == False) or
            (self.tb.IsChecked == False and self.indomaret.IsChecked == False and self.pulsa.IsChecked == False)) :
            MessageBox.Show("Mohon Lengkapi Data Data Diatas")
        elif self.SK.IsChecked == False : 
            MessageBox.Show("Mohon Baca dan Setujui Syarat dan Ketentuan yang berlaku")
        else:
            if self.ComboBoxD.Text == self.ComboBoxD.Items.GetItemAt(0).ToString():
                distri = "Garena"
                t=2000
                k=1
            elif self.ComboBoxD.Text == self.ComboBoxD.Items.GetItemAt(1).ToString():
                distri = "Origin"
                t=1000
                k=1.5
            elif self.ComboBoxD.Text == self.ComboBoxD.Items.GetItemAt(2).ToString():
                distri = "Gamescool"
                t=0
                k=1
            elif self.ComboBoxD.Text == self.ComboBoxD.Items.GetItemAt(3).ToString():
                distri = "Steam Wallet"
                t=0
                k=1.5
            elif self.ComboBoxD.Text == self.ComboBoxD.Items.GetItemAt(4).ToString():
                distri = "Epic Games"
                t=2000
                k=1.5

            if self.h10k.IsChecked:
                biaya=10000
                paket="Rp 10.000"
            elif self.h20k.IsChecked:
                biaya=20000
                paket="Rp 20.000"
            elif self.h50k.IsChecked:
                biaya=50000
                paket="Rp 50.000"
            elif self.h100k.IsChecked:
                biaya=100000
                paket="Rp 100.000"
            elif self.h250k.IsChecked:
                biaya=250000
                paket="Rp 250.000"
            elif self.h500k.IsChecked:
                biaya=500000
                paket="Rp 500.000"
            elif self.h1jt.IsChecked:
                biaya=1000000
                paket="Rp 1.000.000"

            if c == "WFH2020":
                diskon=100
                diskonmax=20000
            elif c == "RAMADHAN" :
                diskon=20
                diskonmax=50000
            elif c == "DIRUMAH" :
                diskon=75
                diskonmax=75000
            else :
                diskon=0
                diskonmax=0

            harga = int(d)*biaya*k+t
            diskonv2 = (harga*diskon/100)
            hargav2 = harga-min([diskonmax,diskonv2])-random.randint(1,101)

            if self.tb.IsChecked:
                MessageBox.Show("Terima Kasih Telah berbelanja di SMAM SHOP \n\n"+
                                "Mohon Lanjutkan Pembayaran untuk transaksi yang telah dilakukan\n"+
                                "Distributor : "+distri+
                                "\nID : "+b+
                                "\nPaket : "+paket+
                                "\n--------------------------------------------------------------------------------------------"+
                                "\nPembayaran dapat dilakukan dengan Mentransfer uang dengan detail berikut\n"+
                                "Jumlah : Rp"+str(hargav2)+
                                "\nTransfer Ke : 0123456789 \n"+
                                "Atas Nama : Aldi Mulyawan\n"+
                                "Detail Transaksi telah dikirimkan ke email berikut : "+a
                                )
            elif self.indomaret.IsChecked:
                MessageBox.Show("Terima Kasih Telah berbelanja di SMAM SHOP \n\n"+
                                "Mohon Lanjutkan Pembayaran untuk transaksi yang telah dilakukan\n"+
                                "Distributor : "+ distri+
                                "\nID : "+b+
                                "\nPaket : "+ paket+
                                "\n--------------------------------------------------------------------------------------------"+
                                "\nPembayaran dapat dilakukan dengan Pembayaran di indomaret/alfamart dengan detail berikut\n"+
                                "Jumlah : Rp"+str(hargav2)+
                                "\nKode : 0123456789 \n"+
                                "Detail Transaksi telah dikirimkan ke email berikut : "+a
                                )
            elif self.pulsa.IsChecked:
                MessageBox.Show("Terima Kasih Telah berbelanja di SMAM SHOP \n\n"+
                                "Mohon Lanjutkan Pembayaran untuk transaksi yang telah dilakukan\n"+
                                "Distributor : "+ distri+
                                "\nID : "+b+
                                "\nPaket : "+ paket+
                                "\n--------------------------------------------------------------------------------------------"+
                                "\nPembayaran dapat dilakukan dengan Mentransfer Pulsa dengan detail berikut\n"+
                                "Jumlah : Rp"+str(hargav2)+
                                "\nNo HP : 081350488901 \n"+
                                "Detail Transaksi telah dikirimkan ke email berikut : "+a
                                )
            pass
        pass
        
    def coupon_Click(self, sender, e):
        MessageBox.Show("Daftar Coupon Hari ini : \n"+
                        "WFH2020 : Cashback 100% dengan Maksimal Cashback Rp 20.000 \n"+
                        "RAMADHAN : Cashback 20% dengan Maksimal Cashback Rp 50.000 \n"+
                        "DIRUMAH : Cashback 75% dengan Maksimal Cashback Rp 75.000"
                        )
        pass

    
    def SK_Click(self, sender, e):
        MessageBox.Show("Syarat dan Ketentuan berbelanja di SMAM SHOP \n"+
                        "1.Setiap Transaksi yang telah di checkout harus segera di bayar maksimal 7x24 jam \n"+
                        "2.Pengembalian uang hanya dilayani 7x24 jam setelah kode dikirimkan \m"+
                        "3.Kesalahan Penulisan ID tidak menjadi tanggung jawab kami \n"+
                        "4.Diharapkan untuk tidak spam ke email\n\n"+
                        "CS : aldismartkid@gmail.com"
                        )
        pass
        
    def harga_Click(self, sender, e):
        c = self.textboxCoupon.Text.ToString()
        d = self.textboxQTY.Text.ToString()


        if (d == "" or self.ComboBoxD.Text == "" or 
            (self.h10k.IsChecked == False and self.h20k.IsChecked == False and self.h50k.IsChecked == False and self.h100k.IsChecked == False and self.h250k.IsChecked == False and self.h500k.IsChecked == False and self.h1jt.IsChecked == False)):
            MessageBox.Show("Mohon Pilih paketan,distributor serta jumlah yang ingin anda beli")
        else:
            if self.ComboBoxD.Text == self.ComboBoxD.Items.GetItemAt(0).ToString():
                distri = "Garena"
                t=2000
                k=1
            elif self.ComboBoxD.Text == self.ComboBoxD.Items.GetItemAt(1).ToString():
                distri = "Origin"
                t=1000
                k=1.5
            elif self.ComboBoxD.Text == self.ComboBoxD.Items.GetItemAt(2).ToString():
                distri = "Gamescool"
                t=0
                k=1
            elif self.ComboBoxD.Text == self.ComboBoxD.Items.GetItemAt(3).ToString():
                distri = "Steam Wallet"
                t=0
                k=1.5
            elif self.ComboBoxD.Text == self.ComboBoxD.Items.GetItemAt(4).ToString():
                distri = "Epic Games"
                t=2000
                k=1.5

            if self.h10k.IsChecked:
                biaya=10000
                paket="Rp 10.000"
            elif self.h20k.IsChecked:
                biaya=20000
                paket="Rp 20.000"
            elif self.h50k.IsChecked:
                biaya=50000
                paket="Rp 50.000"
            elif self.h100k.IsChecked:
                biaya=100000
                paket="Rp 100.000"
            elif self.h250k.IsChecked:
                biaya=250000
                paket="Rp 250.000"
            elif self.h500k.IsChecked:
                biaya=500000
                paket="Rp 500.000"
            elif self.h1jt.IsChecked:
                biaya=1000000
                paket="Rp 1.000.000"

            if c == "WFH2020":
                diskon=100
                diskonmax=20000
            elif c == "RAMADHAN" :
                diskon=20
                diskonmax=50000
            elif c == "DIRUMAH" :
                diskon=75
                diskonmax=75000
            else :
                diskon=0
                diskonmax=0

            harga = int(d)*biaya*k+t
            diskon = (harga*diskon/100)
            diskonv2 = min([diskonmax,diskon])
            hargav2 = harga-min([diskonmax,diskon])
            MessageBox.Show("Detail Biaya : \n"
                            +str(harga)+"\t\tHarga "+d+" buah voucher "+distri+"\n"
                            +str(diskonv2)+"\t\tDiskon Voucher\n"
                            +"---------------------------------------- (Dikurang)\n"
                            +str(hargav2)+"\t\tHarga Total"
                            )

        pass
        
    def paket_Click(self, sender, e):
        paketan=[10000,20000,50000,100000,250000,500000,1000000]
        harga=[]
        if self.ComboBoxD.Text == "":
            MessageBox.Show("Mohon Pilih distributor yang ingin di cek harga paketannya")
        else:
            if self.ComboBoxD.Text == self.ComboBoxD.Items.GetItemAt(0).ToString():
                distri = "Garena"
                t=2000
                k=1
            elif self.ComboBoxD.Text == self.ComboBoxD.Items.GetItemAt(1).ToString():
                distri = "Origin"
                t=1000
                k=1.5
            elif self.ComboBoxD.Text == self.ComboBoxD.Items.GetItemAt(2).ToString():
                distri = "Gamescool"
                t=0
                k=1
            elif self.ComboBoxD.Text == self.ComboBoxD.Items.GetItemAt(3).ToString():
                distri = "Steam Wallet"
                t=0
                k=1.5
            elif self.ComboBoxD.Text == self.ComboBoxD.Items.GetItemAt(4).ToString():
                distri = "Epic Games"
                t=2000
                k=1.5

            for x in range(0,7):
                z=paketan[x]
                y = z*k+t
                harga.append(y)

            MessageBox.Show("Paketan Untuk Distributor "+distri+":"+
                            "\n Rp 10.000 = Rp "+str(harga[0])+
                            "\n Rp 20.000 = Rp "+str(harga[1])+
                            "\n Rp 50.000 = Rp "+str(harga[2])+
                            "\n Rp 100.000 = Rp "+str(harga[3])+
                            "\n Rp 250.000 = Rp "+str(harga[4])+
                            "\n Rp 500.000 = Rp "+str(harga[5])+
                            "\n Rp 1.000.000 = Rp "+str(harga[6])
                            )
        pass



if __name__ == '__main__':
    Application().Run(MyWindow())
