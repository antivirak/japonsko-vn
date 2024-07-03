import os
import csv
import zipfile


def main():
    # fname = '1297296 Demetori - Retrospective Kyoto ~ Japanese Beautiful Barrage.osz'
    # fname = '2197010 Noeliart - Indigo Blue.osz'
    # fname = '1293085 _namirin - Omajinai.osz'
    fname = '919251 _namirin - Hitokoto no Kyori.osz'
    fname = '705499 _namirin - closing eyes.osz'
    fname = '1774306 nekodex - Little Drummer Girl.osz'
    fname = '1203041 cYsmix - Dovregubben\'s Hall (Cut Ver.).osz'
    fname = '1014707 IAHN - Transform (Original Mix).osz'
    if os.path.exists(os.path.join('/Users/cerman/Downloads', fname)):
        with zipfile.ZipFile(os.path.join('/Users/cerman/Downloads', fname), 'r') as z:
            z.extractall(os.path.join('/Users/cerman/Downloads', os.path.splitext(fname)[0]))
    files = os.listdir(os.path.join('/Users/cerman/Downloads', os.path.splitext(fname)[0]))
    osu = [f for f in files if f.endswith('.osu')][0]
    with open(os.path.join('/Users/cerman/Downloads', os.path.splitext(fname)[0], osu), 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    lines = lines[lines.index('[TimingPoints]') + 1:]
    offset_map = {}
    for line in lines:
        if not line:
            break
        # time / ms, beatLength, meter, sampleSet, sampleIndex, volume, uninherited, effects
        id_, offset, *_ = line.split(',')
        offset_map[id_] = offset

    lines = lines[lines.index('[HitObjects]') + 1:]
    with open('beatmap.tsv', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        for line in lines:
            if not line:
                break
            # x, y, time / ms, type, hitSound, objectParams, hitSample
            _, _, offset, _, key, *_ = line.split(',')
            # offset = offset_map.get(id_)
            # if offset:
            #     writer.writerow((offset, 1 if key == '8' else 0))
            writer.writerow((int(offset) / 1000, 1 if key == '8' else 0))


if __name__ == '__main__':
    main()
