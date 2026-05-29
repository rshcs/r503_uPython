from r503u import R503


if __name__ == "__main__":
    print("Running.")
    fp = R503()

    fp.manual_enroll(location=2, num_of_fps=4)
    print(fp.read_index_table())

