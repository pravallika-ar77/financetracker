from config_utils import read_properties

if __name__ == "__main__":
    props = read_properties()
    for key, value in props.items():
        print(f"{key} = {value}")
