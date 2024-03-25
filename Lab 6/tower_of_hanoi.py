def solve_tower_of_hanoi_for(num_of_disks: int, start_rod: int, end_rod: int) -> None:
    if num_of_disks == 1:
        print_move(1, start_rod, end_rod)
    else:
        other_rod = 6 - (start_rod + end_rod)
        solve_tower_of_hanoi_for(num_of_disks - 1, start_rod, other_rod)
        print_move(num_of_disks, start_rod, end_rod)
        solve_tower_of_hanoi_for(num_of_disks - 1, other_rod, end_rod)


def print_move(disk_num: int, start_rod: int, end_rod: int) -> None:
    print(f"move Disk({disk_num}): Rod({start_rod}) => Rod({end_rod})")


if __name__ == "__main__":
    solve_tower_of_hanoi_for(3, 0, 3)
