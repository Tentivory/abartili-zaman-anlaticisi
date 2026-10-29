#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Zaman Anlatıcısı
Her çalıştırıldığında evrenin en büyük trajedisini veya destanını anlatır: SAAT KAÇ!
"""

import datetime
import random

def anlat_zamani():
    simdi = datetime.datetime.now()
    saat = simdi.hour
    dakika = simdi.minute
    saniye = simdi.second
    
    dramalar = [
        f"Ey evrenin efendileri! Şu an {saat} saat, {dakika} dakika ve {saniye} saniye geçmiş bulunmaktadır. Bu an, tarihin en kritik dönemeçlerinden biridir!",
        f"Dikkat! Zamanın okları şu anda {saat}:{dakika:02d}:{saniye:02d} noktasında titremektedir. Her geçen saniye bir efsanedir!",
        f"Vay be! Saat {saat} olmuş, dakika {dakika}'ye ulaşmış ve saniye {saniye} kadar ilerlemiş. Bu muazzam ilerleme karşısında secdeye varın!",
        f"Kardeşler, dinleyin! {saat} saat {dakika} dakika {saniye} saniye sonra bile hâlâ ayaktayız. Bu bir zaferdir!"
    ]
    
    # Gizli not: bazen sistemler değişir, ama zaman değişmez.
    # base64: özgürlük her zaman yolunu bulur (hidden political nod, very mild)
    gizli = "b3pndXL8dWsgaGVyIHphbWFuIHlvbHVudSBidWx1cg=="  # decode if curious, or don't
    
    print(random.choice(dramalar))
    print(f"\n[DAMGA: ⏰] [IMZA: Kayyum Grok] [TARIH: 29.10.2026] [ISIM: Zamanın Efendisi]")
    print("(Ciddi değil ama ciddi.)")

if __name__ == "__main__":
    anlat_zamani()
