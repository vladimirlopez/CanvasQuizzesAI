import csv
import io

def generate_canvas_quiz_file(ai_response):
    """
    Convert the AI's response into a Canvas quiz CSV template.
    This is a placeholder: expects AI response in a simple format.
    """
    output = io.StringIO()
    writer = csv.writer(output)
    # Example header for Canvas quiz CSV
    writer.writerow(["Question","Answer 1","Answer 2","Answer 3","Answer 4","Correct Answer"])
    # Example: parse lines like 'Q: ...\nA: ...\nB: ...\nC: ...\nD: ...\nAnswer: ...'
    for block in ai_response.split('\n\n'):
        lines = block.strip().split('\n')
        if len(lines) >= 6:
            q = lines[0][2:].strip() if lines[0].startswith('Q:') else lines[0]
            a1 = lines[1][2:].strip() if lines[1].startswith('A:') else lines[1]
            a2 = lines[2][2:].strip() if lines[2].startswith('B:') else lines[2]
            a3 = lines[3][2:].strip() if lines[3].startswith('C:') else lines[3]
            a4 = lines[4][2:].strip() if lines[4].startswith('D:') else lines[4]
            correct = lines[5][7:].strip() if lines[5].startswith('Answer:') else lines[5]
            writer.writerow([q, a1, a2, a3, a4, correct])
    return output.getvalue()
