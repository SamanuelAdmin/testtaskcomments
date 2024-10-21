function setReplyID(id, text) {
    text = text.replace(/[\r\n]+/g, ' ');

    if (text.length > 50){
        text = text.slice(0, 50) + "...";
    }

    document.getElementById("replyID").value = id;
    document.getElementById("commentReplyField").style.display = "flex";
    document.getElementById("repliedCommentText").textContent = text;
    document.getElementById("leaveCommentButton").textContent = "Leave your reply";
}

function restoreComment() {
    document.getElementById("leaveCommentButton").textContent = "Leave your comment";
    document.getElementById("commentReplyField").style.display = "none";

}