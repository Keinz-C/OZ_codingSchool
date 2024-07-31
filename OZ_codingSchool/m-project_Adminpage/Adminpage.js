//updateTime함수는 현재 시간을 가져와 형식에 맞춰 문자열로 변경한다.
function updateTime() {
  const now = new Date(); // new Date 객체는 js에 Date객체를 생성하고, 현재 날짜와 시간 정보를 포함한다.
  const year = now.getFullYear(); // getFullYear은 현재 연도를 가져온다
  const month = (now.getMonth() + 1).toString().padStart(2, '0');
  const day = now.getDate().toString().padStart(2, '0');
  const hours = now.getHours().toString().padStart(2, '0');
  const minutes = now.getMinutes().toString().padStart(2, '0');
  const seconds = now.getSeconds().toString().padStart(2, '0');
  const timeString = `${year}년${month}월${day}일 ${hours}:${minutes}:${seconds}`;

  document.getElementById('timeDisplay').textContent = timeString;
}
setInterval(updateTime, 1000); // 매 1초마다 updateTime 함수 호출하여 내부 객체를 실행시킨다.

// 페이지 로드 시 즉시 시간을 표시하기 위해 초기 호출
updateTime();

let currentPage = 1; //currentPage 현재 페이지를 추적한다.
        const totalPages = 3; // totalPages는 전체 페이지 수를 정의한다.

        function updatePagination() { // updatePagination 함수는 현재 페이지를 기준으로 이전과 다음 버튼의 상태를 업데이트한다
            document.getElementById('previous').parentElement.classList.toggle('disabled', currentPage === 1);
            document.getElementById('next').parentElement.classList.toggle('disabled', currentPage === totalPages);
        }

        function changePage(page) { // changePage 함수는 페이지를 변경시킨다.
            if (page < 1 || page > totalPages) return;
            currentPage = page; 
            updatePagination();
            console.log(`Current Page: ${currentPage}`); // 페이지 변경 시 실행할 코드
        }
        // changePage로 페이지를 변경하고, currentPage로 현재 페이지를 호출받아 updatePagination 함수를 실행한다.

        // 페이지 로드 시 초기 상태 업데이트
        updatePagination();


// dark모드와 light모드를 만들어보자

function setDarkMode(){
  document.body.classList.remove('light-mode');
  document.body.classList.add('dark-mode');
}

function setLightMode(){
  document.body.classList.remove('dark-mode');
  document.body.classList.add('light-mode');
}