import os, time, sys
from version import version
from color import color
class UI:

	@classmethod
	def slowPrinting(cls, text):
		for letter in text:
			time.sleep(.002)
			print(letter, end="", flush=True)
		print("")
	@classmethod
	def logo(cls):
		cls.slowPrinting("░█████╗░░██╗░░░░░░░██╗░█████╗░  ░██████╗███████╗██╗░░░░░███████╗  ██████╗░░█████╗░████████╗")
		cls.slowPrinting("██╔══██╗░██║░░██╗░░██║██╔══██╗  ██╔════╝██╔════╝██║░░░░░██╔════╝  ██╔══██╗██╔══██╗╚══██╔══╝")
		cls.slowPrinting("██║░░██║░╚██╗████╗██╔╝██║░░██║  ╚█████╗░█████╗░░██║░░░░░█████╗░░  ██████╦╝██║░░██║░░░██║░░░")
		cls.slowPrinting("██║░░██║░░████╔═████║░██║░░██║  ░╚═══██╗██╔══╝░░██║░░░░░██╔══╝░░  ██╔══██╗██║░░██║░░░██║░░░")
		cls.slowPrinting("╚█████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝  ██████╔╝███████╗███████╗██║░░░░░  ██████╦╝╚█████╔╝░░░██║░░░")
		cls.slowPrinting("░╚════╝░░░░╚═╝░░░╚═╝░░░╚════╝░  ╚═════╝░╚══════╝╚══════╝╚═╝░░░░░  ╚═════╝░░╚════╝░░░░╚═╝░░░")
		cls.slowPrinting(f"                                {color.purple}Version: {version}{color.reset}")
		time.sleep(0.5)
		print()

	@classmethod
	def start(cls):
		cls.slowPrinting("╔═══════════════════════════════╗")
		print()
		cls.slowPrinting(f"       {color.purple}[1]{color.reset} Tải dữ liệu Hiện Có")
		cls.slowPrinting(f"       {color.purple}[2]{color.reset} Tạo dữ liệu mới")
		cls.slowPrinting(f"       {color.purple}[3]{color.reset} Thông tin bổ sung")
		cls.slowPrinting(f"       {color.purple}[4]{color.reset} Thoát")
		print()
		cls.slowPrinting("╚═══════════════════════════════╝")
	@classmethod
	def newData(cls):
		cls.slowPrinting("╔═══════════════════════════════════════════╗")
		print()
		cls.slowPrinting(" [0] Thoát và lưu")
		cls.slowPrinting(" [1] Thay đổi tất cả cài đặt")
		cls.slowPrinting(" [2] Thay Đổi Account Token")
		cls.slowPrinting(" [3] Thay đổi kênh")
		cls.slowPrinting(" [4] Thay đổi chế độ Pray")
		cls.slowPrinting(" [5] Thay đổi chế độ đá quý")
		cls.slowPrinting(" [6] Thay đổi chế độ Exp")
		cls.slowPrinting(" [7] Thay đổi chế độ ngủ")
		cls.slowPrinting(" [8] Thay đổi cài đặt Webhook")
		cls.slowPrinting(" [9] Thay đổi lệnh Selfbot")
		cls.slowPrinting(" [10] Thay đổi chế độ tự động nhận phần thưởng")
		cls.slowPrinting(" [11] Thay đổi thời gian dừng")
		cls.slowPrinting(f" [12] Thay đổi chế độ sell")
		cls.slowPrinting(" [13] Thay đổi chế độ chuyển kênh")
		cls.slowPrinting(" [14] Thay đổi giải mã xác thực")
		print()
		cls.slowPrinting("╚═══════════════════════════════════════════╝")
	@classmethod
	def info(cls):
		cls.slowPrinting(f"{color.purple}╔═════════════════Support════════════════╗{color.reset}")
		cls.slowPrinting(f"\t{color.purple}https://discord.gg/9CzeBKhsmf{color.reset}")
		cls.slowPrinting(" ")
		cls.slowPrinting(f"{color.purple}╔═══════════════════════════════════════════════════════════════════════════Disclaimer═══════════════════════════════════════════════════════════╗{color.reset}")
		cls.slowPrinting(f"\t{color.purple}Self Bot Bản Gốc Được Làm Bởi Sudo-Nizel Và Ahihiyou20, Cải tiến và việt hoá bởi Minerwolf, Không Bán Code Dưới Mọi Hình Thức. Open source In Github")
		cls.slowPrinting(" ")
		cls.slowPrinting(f'{color.purple}╔═════════════════Credit═════════════════╗{color.reset}')
		cls.slowPrinting(f'\t{color.purple} [Developer] {color.reset} Sudo-Nizel')
		cls.slowPrinting(f'\t{color.purple} [Developer] {color.reset} ahihiyou20')
		cls.slowPrinting(f'\t{color.purple} [Developer] {color.reset} Minerwolf')
		cls.slowPrinting(" ")
		cls.slowPrinting(f'{color.purple}╔═════════════════════════Selfbot Commands════════════════════════╗{color.reset}')
		cls.slowPrinting("\t{Prefix}send {Message} [Send Your Provied Message}")
		cls.slowPrinting("\t{Prefix}restart [Restart The Selfbot]")
		cls.slowPrinting("\t{Prefix}exit [Stop The Selfbot]")
		cls.slowPrinting("\t{Prefix}sm {on/off} [Turn On Or Off Sleep Mode]")
		cls.slowPrinting("\t{Prefix}em {on/off} [Turn On Or Off Exp Mode]")
		cls.slowPrinting("\t{Prefix}pm {on/off} [Turn On Or Off Pray Mode]")
		cls.slowPrinting("\t{Prefix}gm {on/off} [Turn On Or Off Gems Mode]")
		cls.slowPrinting("\t{Prefix}gems [Use Gems]")
		cls.slowPrinting(" ")
		cls.slowPrinting("{Prefix} == Your Prefix")
		cls.slowPrinting(" ")
		cls.slowPrinting("Note: publicly available at github, No trading in any form")
		time.sleep(0.5)
		cls.slowPrinting("Press Enter To Exit")
		input()
