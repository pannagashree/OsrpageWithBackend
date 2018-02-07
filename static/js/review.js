function addFeedback()
{
	$.ajax({url:"review.html",success:function(result){
		var iDiv=document.createElement('div');
		console.log(iDiv.textContent);
		iDiv.className="reviews";
		var infoDiv=document.createElement('div');
		infoDiv.className="info";
		iDiv.appendChild(infoDiv);
		var contDiv=document.createElement('div');
		contDiv.className="cont";
		iDiv.appendChild(contDiv);
		document.getElementsByClassName("review_section")[0].appendChild(iDiv);
		var modicont=$('.review_section').html();
		localStorage.setItem('modified',modicont);
	}})
}
$(document).ready(function(){
	if(localStorage.getItem('modified'))
		$('.review_section').html(localStorage.getItem('modified'));
})
