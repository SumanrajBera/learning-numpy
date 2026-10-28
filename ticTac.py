import numpy as np
import streamlit as st

# ----------------------------
# Initialize session state
# ----------------------------
if "board" not in st.session_state:
    st.session_state.board = np.zeros((3, 3), dtype=int)
    st.session_state.current = 1  # 1 = X, -1 = O
    st.session_state.result = None

symbols = {0: " ", 1: "X", -1: "O"}


# ----------------------------
# Winner checking logic
# ----------------------------
def check_winner(b):
    # Rows & columns
    if 3 in np.sum(b, axis=1) or 3 in np.sum(b, axis=0):
        return "X"
    if -3 in np.sum(b, axis=1) or -3 in np.sum(b, axis=0):
        return "O"

    # Diagonals
    if np.trace(b) == 3 or np.trace(np.fliplr(b)) == 3:
        return "X"
    if np.trace(b) == -3 or np.trace(np.fliplr(b)) == -3:
        return "O"

    # Draw
    if not 0 in b:
        return "DRAW"

    return None


# ----------------------------
# Streamlit UI
# ----------------------------
st.set_page_config(page_title="Tic-Tac-Toe", layout="centered")

st.title("Tic-Tac-Toe")

# Custom CSS for the game board
st.markdown(
    """
<style>
/* Make each cell look like a proper square */
div.stButton > button {
    width: 100%;
    height: 120px;
    font-size: 42px;
    font-weight: bold;
    border: 2px solid #64748b;
    border-radius: 10px;
    background-color: #f8fafc;
    color: #0f172a;
    transition: background-color 0.2s ease;
}

/* Hover effect */
div.stButton > button:hover:not(:disabled) {
    background-color: #dbeafe;
    border-color: #2563eb;
    color: #1d4ed8;
}

/* Keep played cells visible */
div.stButton > button:disabled {
    opacity: 1;
    background-color: #e2e8f0;
    color: #0f172a;
    border-color: #64748b;
}

/* Add space between cells */
div[data-testid="stHorizontalBlock"] {
    gap: 10px;
}
</style>
""",
    unsafe_allow_html=True,
)

# Game status
if st.session_state.result:
    if st.session_state.result == "DRAW":
        st.success("It's a draw!")
    else:
        st.success(f"{st.session_state.result} wins!")
else:
    turn = "X" if st.session_state.current == 1 else "O"
    st.info(f"It's {turn}'s turn")

# 3x3 board
cols = st.columns(3, gap="small")

for i in range(3):
    for j in range(3):
        with cols[j]:
            cell_value = symbols[st.session_state.board[i, j]]

            is_disabled = (
                st.session_state.board[i, j] != 0 or st.session_state.result is not None
            )

            if st.button(
                cell_value if cell_value != " " else " ",
                key=f"{i}-{j}",
                disabled=is_disabled,
                use_container_width=True,
            ):
                st.session_state.board[i, j] = st.session_state.current

                result = check_winner(st.session_state.board)

                if result:
                    st.session_state.result = result
                else:
                    st.session_state.current *= -1

                st.rerun()

# Restart
if st.button("Restart Game", use_container_width=True):
    st.session_state.board = np.zeros((3, 3), dtype=int)
    st.session_state.current = 1
    st.session_state.result = None
    st.rerun()
