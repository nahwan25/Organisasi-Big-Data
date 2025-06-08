from cassandra.cluster import Cluster

def ambil_data_dari_cassandra():
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect('tubes_orbid')

    query = "SELECT id_karyawan, nama_lengkap, jam_kerja_per_bulan FROM data_karyawan;"
    rows = session.execute(query)

    hasil = []
    for r in rows:
        hasil.append({
            "sumber": "Cassandra",
            "id_karyawan": r.id_karyawan,
            "nama_lengkap": r.nama_lengkap,
            "jam_kerja_per_bulan": r.jam_kerja_per_bulan
        })

    return hasil