from r503u import R503


if __name__ == "__main__":
    print("Running.")
    fp = R503()
    # fp.empty_finger_lib()
    fp.simplified_enroll()
    print(fp.read_index_table())
    # print(fp.search())

