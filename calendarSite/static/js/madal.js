// JavaScript Document
'use strict'

{
	const open = document.getElementById('open');
	const close = document.getElementById('close');
	const modal = document.getElementById('modal');
	const mask = document.getElementById('mask');
	
	open.addEventListener('click',()=>{
		modal.classList.remove('hidden');
		mask.classList.remove('hidden');
	});
	
	close.addEventListener('click',()=>{
		modal.classList.add('hidden');
		mask.classList.add('hidden');
	});
	
	mask.addEventListener('click',()=>{
		//modal.classList.add('hidden');
		//mask.classList.add('mask');
		close.click();
	});
}