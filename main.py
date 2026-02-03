"""Study Log - aplikasi sederhana untuk mencatat aktivitas belajar.

Fitur yang diimplementasikan:
- `tambah_catatan()` : input mapel, topik, durasi (menit) -> simpan ke list `catatan`
- `lihat_catatan()`  : tampilkan semua catatan rapi (juga menampilkan progres target jika ada)
- `total_waktu()`    : hitung total durasi dari semua catatan
- `set_target_harian()`: fitur tambahan untuk mengatur target harian (menit)

Struktur data: `catatan` adalah list of dict sederhana untuk kemudahan pemula.
"""
import json

catatan = []
target_harian = None


def tambah_catatan():
	"""Minta input mapel, topik, dan durasi (menit) lalu simpan ke `catatan`."""
	mapel = input("Mapel: ").strip()
	topik = input("Topik: ").strip()
	while True:
		dur = input("Durasi belajar (menit): ").strip()
		try:
			dur = int(dur)
			if dur <= 0:
				raise ValueError
			break
		except ValueError:
			print("Masukkan angka bulat positif untuk durasi (menit).")

	catatan.append({
		"mapel": mapel,
		"topik": topik,
		"durasi": dur,
	})
	print("Catatan berhasil ditambahkan.")


def lihat_catatan():
	"""Tampilkan semua catatan belajar dengan rapi. Tampilkan pesan bila kosong."""
	if not catatan:
		print("Belum ada catatan belajar.")
		return

	print("\nDaftar Catatan Belajar:")
	print("-" * 40)
	for i, c in enumerate(catatan, start=1):
		print(f"{i}. {c['mapel']} - {c['topik']} ({c['durasi']} menit)")
	print("-" * 40)

	total = total_waktu()
	print(f"Total waktu belajar: {total} menit")
	if target_harian:
		persen = total * 100 / target_harian
		print(f"Target harian: {target_harian} menit — tercapai {persen:.1f}%")
	else:
		print("Target harian: belum diatur. Gunakan menu 'Set Target Harian'.")


def total_waktu():
	"""Kembalikan total durasi (menit) dari semua catatan."""
	return sum(item.get("durasi", 0) for item in catatan)


def set_target_harian():
	"""Set target harian dalam menit."""
	global target_harian
	while True:
		t = input("Masukkan target harian (menit): ").strip()
		try:
			t = int(t)
			if t <= 0:
				raise ValueError
			target_harian = t
			print(f"Target harian diset: {t} menit.")
			break
		except ValueError:
			print("Masukkan angka bulat positif untuk target.")


def main():
	while True:
		print("\n📖📖📖 Study Log 📖📖📖")
		
		print("1. Tambah catatan ➕")
		print("2. Lihat catatan 🔍")
		print("3. Atur Target Harian ⏳")
		print("4. Total waktu 🕐")
		print("5. Exit 🚪➡️")
		pilihan = input("Pilih (1-5): ").strip()

		if pilihan == "1":
			tambah_catatan()
		elif pilihan == "2":
			lihat_catatan()
		elif pilihan == "3":
			set_target_harian()
		elif pilihan == "4":
			print(f"Total waktu belajar sekarang: {total_waktu()} menit")
		elif pilihan == "5":
			print("Terima kasih — sampai jumpa!")
			break
		else:
			print("Pilihan tidak dikenal. Silakan pilih 1-5.")


if __name__ == "__main__":
	main()

