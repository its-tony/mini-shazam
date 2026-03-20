import argparse

from src.database import SongDatabase
from src.recognize import recognize, record_and_recognize
from src.utils import load_audio


def build_database(songs_dir):
    db = SongDatabase()
    db.index_directory(songs_dir)
    return db


def main():
    parser = argparse.ArgumentParser(description="Mini Shazam demo")
    parser.add_argument(
        "--songs-dir",
        default="songs",
        help="Directory with .wav songs to index",
    )
    parser.add_argument(
        "--clip",
        help="Optional .wav clip to recognize instead of recording from the microphone",
    )
    parser.add_argument(
        "--duration",
        type=int,
        default=5,
        help="Recording duration in seconds when using the microphone",
    )
    args = parser.parse_args()

    db = build_database(args.songs_dir)

    if args.clip:
        audio, sample_rate = load_audio(args.clip)
        best_name, best_score, all_scores = recognize(audio, sample_rate, db)
        if best_name:
            print(f"Match: {best_name} (score: {best_score})")
        else:
            print("No match found.")

        if all_scores:
            print("All scores:")
            for name, score in sorted(all_scores.items(), key=lambda item: -item[1]):
                print(f"  {name}: {score}")
        return

    record_and_recognize(db, duration=args.duration)


if __name__ == "__main__":
    main()
