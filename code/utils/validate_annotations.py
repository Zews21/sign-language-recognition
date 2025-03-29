import os
import yaml

DATA_PATH = r".\data"
CLASS_NAMES = ['Hello', 'Yes', 'No', 'Thank You', 'I Love You']
NC = 5  # Number of classes


def validate_annotations():
    errors = []
    valid_count = 0
    total_files = 0

    for split in ['train', 'test']:
        label_dir = os.path.join(DATA_PATH, 'labels', split)
        image_dir = os.path.join(DATA_PATH, 'images', split)

        if not os.path.exists(label_dir):
            errors.append(f"Missing label directory: {label_dir}")
            continue

        for label_file in os.listdir(label_dir):
            total_files += 1
            label_path = os.path.join(label_dir, label_file)
            image_path = os.path.join(image_dir, label_file.replace('.txt', '.jpg'))

            # Check 1: Corresponding image exists
            if not os.path.exists(image_path):
                errors.append(f"Missing image for {label_file}")
                continue

            with open(label_path, 'r') as f:
                lines = f.readlines()

            for line_num, line in enumerate(lines, 1):
                parts = line.strip().split()

                # Check 2: Valid number of values
                if len(parts) != 5:
                    errors.append(
                        f"{label_file} line {line_num}: Invalid annotation format. "
                        f"Expected 5 values, got {len(parts)}"
                    )
                    continue

                try:
                    class_id = int(parts[0])
                    coords = list(map(float, parts[1:]))
                except ValueError:
                    errors.append(
                        f"{label_file} line {line_num}: Non-numeric values detected"
                    )
                    continue

                # Check 3: Valid class ID
                if not (0 <= class_id < NC):
                    errors.append(
                        f"{label_file} line {line_num}: Invalid class ID {class_id}. "
                        f"Allowed range: 0-{NC - 1}"
                    )

                # Check 4: Valid coordinates (0-1)
                for i, val in enumerate(coords):
                    if not (0.0 <= val <= 1.0):
                        errors.append(
                            f"{label_file} line {line_num}: Coordinate {i + 1} out of range. "
                            f"Value: {val}, should be 0-1"
                        )

            valid_count += 1

    print(f"\nValidation Complete:")
    print(f"Scanned {total_files} label files")
    print(f"Valid files: {valid_count}/{total_files}")

    if errors:
        print("\nFound errors:")
        for error in errors[:10]:
            print(f" - {error}")
        if len(errors) > 10:
            print(f"...and {len(errors) - 10} more errors")
        print("\nAction required:")
        print("1. Fix the reported annotation issues")
        print("2. Re-run this validation script")
    else:
        print("All annotations are valid!")


if __name__ == "__main__":
    validate_annotations()