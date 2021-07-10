import sys

def update_progress_bar(complete,
                        n_iterations,
                        block_shape="█",
                        remaining_shape=".",
                        len_bar=20):

    progress = complete / n_iterations

    rounded_progress = int(round(len_bar * progress))

    draw_progress = block_shape * rounded_progress + remaining_shape * (
        len_bar - rounded_progress)

    text = f"\r|{draw_progress}| {complete}/{n_iterations} {progress*100:2.2f}% "

    sys.stdout.write(text)
    sys.stdout.flush()