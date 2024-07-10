import os
import csv
import sys
import zipfile


def main(fname):
    base_name = os.path.splitext(fname)[0]
    if os.path.exists(fname):
        with zipfile.ZipFile(fname, 'r') as z:
            z.extractall(base_name)
    if not os.path.exists(base_name):
        raise FileNotFoundError(f'Paths {fname} and {base_name} not found. Please provide one of them as an input.')

    files = os.listdir(base_name)
    osu = [f for f in files if f.endswith('.osu')][0]  # take only one in case of multiple difficulties
    with open(os.path.join(base_name, osu), 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    # lines = lines[lines.index('[TimingPoints]') + 1:]
    # offset_map = {}
    # for line in lines:
    #     if not line:
    #         break
    #     # time / ms, beatLength, meter, sampleSet, sampleIndex, volume, uninherited, effects
    #     offset, beat_len, *_ = line.split(',')
    #     offset_map[offset] = beat_len

    lines = lines[lines.index('[HitObjects]') + 1:]
    with open('beatmap.tsv', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        for line in lines:
            if not line:
                break
            # header:
            # x, y, time / ms, type, hitSound, objectParams, hitSample
            _, _, offset, _, key, *_ = line.split(',')
            writer.writerow((int(offset) / 1000, 1 if key == '8' else 0))


if __name__ == '__main__':
    main(
        sys.argv[1] if len(sys.argv) > 1 and sys.argv[1]
        else '1014707 IAHN - Transform (Original Mix).osz'
    )
