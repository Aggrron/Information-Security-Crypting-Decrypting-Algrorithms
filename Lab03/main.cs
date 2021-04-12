using System;
using AesLib;

namespace AesDemoConsole
{
  class Class1
  {
    [STAThread]
    static void Main(string[] args)
    {
      byte[] plainText = new byte[] {0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77,
                                      0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff};
      
      byte[] cipherText = new byte[16];
      byte[] decipheredText = new byte[16];
      
      byte[] keyBytes = new byte[] {0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07,
                                     0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f,
                                     0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17};
    
      Aes a = new Aes(Aes.KeySize.Bits192, keyBytes);
      
      Console.WriteLine("\nThe plaintext is: ");
      DisplayAsBytes(plainText);

      Console.WriteLine("\nUsing a " + Aes.KeySize.Bits192.ToString() + "-key of: ");
      DisplayAsBytes(keyBytes);
     
      a.Cipher(plainText, cipherText);

      Console.WriteLine("\nThe resulting ciphertext is: ");
      DisplayAsBytes(cipherText);

      a.InvCipher(cipherText, decipheredText);

      Console.WriteLine("\nAfter deciphering the ciphertext, the result is: ");
      DisplayAsBytes(decipheredText);

      Console.WriteLine("\nDone");
      Console.ReadLine();
    }  // Main()

    static void DisplayAsBytes(byte[] bytes)
    {
      for (int i = 0; i < bytes.Length; ++i)
      {
        Console.Write(bytes[i].ToString("x2") + " " );
        if (i > 0 && i % 16 == 0) Console.Write("\n");
      }
      Console.WriteLine("");
    }  // DisplayAsBytes()

  }  // class Class1
}  // ns AesDemoConsole