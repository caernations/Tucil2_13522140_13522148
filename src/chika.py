import pygame
import sys
import time

# Inisialisasi pygame
pygame.init()

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Lebar dan tinggi layar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quadratic Bezier Curve")

# Fungsi draw_point untuk menggambar titik
def draw_point(point, color):
    pygame.draw.circle(screen, color, (int(point[0]), int(point[1])), 5)

# Fungsi bezier_curve_divide_and_conquer untuk menghitung kurva Bézier menggunakan algoritma divide and conquer
def bezier_curve_divide_and_conquer(points, iterations):
    if iterations == 0:
        return [points[0], points[2]]
    
    # Hitung titik tengah
    Q0 = [(points[0][0] + points[1][0]) / 2, (points[0][1] + points[1][1]) / 2]
    Q1 = [(points[1][0] + points[2][0]) / 2, (points[1][1] + points[2][1]) / 2]
    R0 = [(Q0[0] + Q1[0]) / 2, (Q0[1] + Q1[1]) / 2]

    # Rekursi untuk titik baru
    left_curve = bezier_curve_divide_and_conquer([points[0], Q0, R0], iterations - 1)
    right_curve = bezier_curve_divide_and_conquer([R0, Q1, points[2]], iterations - 1)

    return left_curve + right_curve[1:]

# Fungsi bezier_curve_brute_force untuk menghitung kurva Bézier menggunakan algoritma brute force
def bezier_curve_brute_force(points, iterations):
    if iterations == 0:
        return [points[0], points[2]]

    # Hitung titik-titik antara
    S0 = [(points[0][0] + points[1][0]) / 2, (points[0][1] + points[1][1]) / 2]
    S1 = [(points[1][0] + points[2][0]) / 2, (points[1][1] + points[2][1]) / 2]
    S2 = [(S0[0] + S1[0]) / 2, (S0[1] + S1[1]) / 2]

    # Rekursi untuk titik baru
    left_curve = bezier_curve_brute_force([points[0], S0, S2], iterations - 1)
    right_curve = bezier_curve_brute_force([S2, S1, points[2]], iterations - 1)

    return left_curve + right_curve[1:]

# Fungsi untuk menampilkan kurva Bézier
def draw_bezier_curve(curve, color):
    for i in range(len(curve) - 1):
        pygame.draw.line(screen, color, (int(curve[i][0]), int(curve[i][1])), (int(curve[i + 1][0]), int(curve[i + 1][1])), 2)

# Fungsi untuk menampilkan tahap demi tahap pembentukan kurva Bézier
def draw_bezier_steps(points, color):
    # Titik awal dan akhir
    draw_point(points[0], color)
    draw_point(points[-1], color)

    # Tahap 1
    pygame.draw.line(screen, color, (int(points[0][0]), int(points[0][1])), (int(points[1][0]), int(points[1][1])), 2)
    pygame.draw.line(screen, color, (int(points[1][0]), int(points[1][1])), (int(points[2][0]), int(points[2][1])), 2)

    # Tahap 2
    Q0 = [(points[0][0] + points[1][0]) / 2, (points[0][1] + points[1][1]) / 2]
    Q1 = [(points[1][0] + points[2][0]) / 2, (points[1][1] + points[2][1]) / 2]
    R0 = [(Q0[0] + Q1[0]) / 2, (Q0[1] + Q1[1]) / 2]
    draw_point(Q0, color)
    draw_point(Q1, color)
    draw_point(R0, color)
    pygame.draw.line(screen, color, (int(points[0][0]), int(points[0][1])), (int(Q0[0]), int(Q0[1])), 2)
    pygame.draw.line(screen, color, (int(Q0[0]), int(Q0[1])), (int(R0[0]), int(R0[1])), 2)
    pygame.draw.line(screen, color, (int(R0[0]), int(R0[1])), (int(Q1[0]), int(Q1[1])), 2)
    pygame.draw.line(screen, color, (int(Q1[0]), int(Q1[1])), (int(points[2][0]), int(points[2][1])), 2)

# Fungsi utama
def main():
    # Input titik awal, titik kontrol, dan titik akhir dari pengguna
    P0 = list(map(int, input("Masukkan koordinat titik awal (pisahkan dengan spasi): ").split()))
    P1 = list(map(int, input("Masukkan koordinat titik kontrol (pisahkan dengan spasi): ").split()))
    P2 = list(map(int, input("Masukkan koordinat titik akhir (pisahkan dengan spasi): ").split()))
    
        # Input jumlah iterasi
    iterations = int(input("Masukkan jumlah iterasi: "))

    # Menghitung kurva Bézier menggunakan algoritma divide and conquer
    start_time = time.time()
    bezier_curve_dc = bezier_curve_divide_and_conquer([P0, P1, P2], iterations)
    dc_execution_time = time.time() - start_time

    # Menghitung kurva Bézier menggunakan algoritma brute force
    start_time = time.time()
    bezier_curve_bf = bezier_curve_brute_force([P0, P1, P2], iterations)
    bf_execution_time = time.time() - start_time

    # Menampilkan hasil
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)

        # Menampilkan kurva Bézier hasil algoritma divide and conquer
        draw_bezier_curve(bezier_curve_dc, BLACK)

        # Menampilkan kurva Bézier hasil algoritma brute force
        draw_bezier_curve(bezier_curve_bf, RED)

        # Menampilkan titik-titik kontrol
        draw_point(P0, BLACK)
        draw_point(P1, BLACK)
        draw_point(P2, BLACK)

        # Menampilkan visualisasi proses pembentukan kurva Bézier menggunakan algoritma divide and conquer
        draw_bezier_steps([P0, P1, P2], BLUE)

        # Menampilkan visualisasi proses pembentukan kurva Bézier menggunakan algoritma brute force
        draw_bezier_steps([P0, P1, P2], GREEN)

        pygame.display.flip()

    pygame.quit()

    print(f"Execution time (divide and conquer): {dc_execution_time} seconds")
    print(f"Execution time (brute force): {bf_execution_time} seconds")

if __name__ == "__main__":
    main()

