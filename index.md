---
marp: true
theme: pbl
class: invert
---

<style scoped>
.preload-container {
    position: relative;
    display: flex;
    flex-wrap: wrap;
    margin: 0.5rem auto;
    width: 90%;
    height: auto;
    overflow: hidden;
    justify-content: center;
    gap: 10px;
    padding: 0.5rem;
    border-radius: 1rem;
    box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.5);
    background-color: rgba(255, 255, 255, 0.05);
}

.image-set {
    opacity: 0;
    animation: fadeIn 0.5s ease-in 1s forwards;
}

@keyframes fadeIn {
    to {
        opacity: 1;
    }
}

.preload-container img {
    width: 8%;
    height: auto;
    object-fit: cover;
    opacity: 0.5;
    border-radius: 10px;
}

blockquote {
    margin: 0.5rem auto;
    width: 90%;
    border-radius: 1rem;
    box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.5);
    background-color: rgba(255, 255, 255, 0.05);
    padding: 0.5rem;
}

.spinner-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: transparent;
    z-index: 10;
    animation: hideSpinner 0.5s 1s forwards;
}

@keyframes hideSpinner {
    to {
        opacity: 0;
        visibility: hidden;
    }
}

.lds-ring {
    color: #1c4c5b;
}
.lds-ring,
.lds-ring div {
    box-sizing: border-box;
}
.lds-ring {
    display: inline-block;
    position: relative;
    width: 80px;
    height: 80px;
}
.lds-ring div {
    box-sizing: border-box;
    display: block;
    position: absolute;
    width: 64px;
    height: 64px;
    margin: 8px;
    border: 8px solid currentColor;
    border-radius: 50%;
    animation: lds-ring 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;
    border-color: currentColor transparent transparent transparent;
}
.lds-ring div:nth-child(1) {
    animation-delay: -0.45s;
}
.lds-ring div:nth-child(2) {
    animation-delay: -0.3s;
}
.lds-ring div:nth-child(3) {
    animation-delay: -0.15s;
}
@keyframes lds-ring {
    from {
        transform: rotate(0deg);
    }
    to {
        transform: rotate(360deg);
    }
}

sub {
    position: absolute;
    bottom: 25px;
    right: 15px;
}
</style>

<div class="spe-star opac"></div>
<div class="sky stitle">
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
</div>

<sub>build <span class="build-time"></span></sub>

---

<div class="spe-star opac"></div>
<div class="sky stitle">
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
</div>

<div class="title slowup">스마트 멀티탭에 관한 연구</div>
<div class="sub-title slowup" >Research on Smart Multi-Tap</div>

<div class="speaker slowup">

## 발표자

<h6 style="padding-left: 70px;"> 박준영</h4>

</div>

<div class="progress">
  <div class="bar" style="--start-progress: -1;">
</div>

---

<div class="spe-star"></div>

<div class="header slowup">
📋 <span class="sub0"> 목차 </span>
</div>

<div class="content slowup">

<div class="text slowup" style="--order: 2;">
    <h2 class="slowup" style="--order: 2.2;">서론</h2>
    <ul>
        <li class="slowup" style="--order: 2.4;">연구 배경 및 목적</li>
        <li class="slowup" style="--order: 2.6;">기존 제품 분석</li>
    </ul>
    <h2 class="slowup" style="--order: 2.8;">설계 및 구현</h2>
    <ul>
        <li class="slowup" style="--order: 3;">소프트웨어 및 하드웨어</li>
        <li class="slowup" style="--order: 3.2;">주요 기능</li>
    </ul>

</div>

<div class="text slowup" style="--order: 3.4;">
    <h2 class="slowup" style="--order: 3.6;">실험 및 결과</h2>
    <ul>
        <li class="slowup" style="--order: 3.8;">실험 분석 및 해결 방안</li>
        <div style="margin-top: 3.25rem;"></div>
    </ul>
    <h2 class="slowup" style="--order: 4;">고찰 및 결론</h2>
    <ul>
        <li class="slowup" style="--order: 4.2;">연구 결과 분석</li>
        <li class="slowup" style="--order: 4.4;">한계점 및 개선 방안</li>
        <li class="slowup" style="--order: 4.6;">결론</li>
    </ul>

</div>
</div>

<div class="progress">
  <div class="bar" style="--start-progress: 0;">
</div>

---

<div class="spe-star opac"></div>
<div class="sky stitle">
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
</div>

<div class="half">
<div class="img slowup" style="--order: 0; flex: 0.5">
<img src="./reimg/main.webp" style="width: 90%;">
</div>

<div class="text slowup" style="--order: 1;">
    <h1 class="sub1 slowup" style="--order: 1.2;"><span class="sub1"> 서론 </span></h1>
    <ul>
        <li class="slowup" style="--order: 1.7;">연구 배경 및 목적</li>
        <li class="slowup" style="--order: 2.2;">기존 제품 분석</li>
    </ul>
</div>
</div>

<div class="progress">
  <div class="bar" style="--start-progress: 1;">
</div>

---

<div class="spe-star"></div>

<div class="header slowup">
🚀 <span class="sub1"> 서론 </span> 🔹 <strong>연구 배경 및 목적</strong>
</div>

<div class="content slowup" style="--img-flex: 0.4; --text-flex: 0.6">

<div class="text slowup" style="--order: 2;">
    <h3 class="slowup" style="--order: 2.2;">연구배경</h3>
    <ul>
        <li class="slowup" style="--order: 2.4;">전기는 현대 사회에서의 필수적인 요소</li>
        <li class="slowup" style="--order: 2.6;">전체 화재의 약 30%가 전기화재</li>
        <li class="slowup" style="--order: 2.8;">멀티탭은 가까운 전기기기 중 하나</li>
    </ul>
    <h3 class="slowup" style="--order: 3.3;">목적</h3>
    <ul>
        <li class="slowup" style="--order: 3.5;">조금 더 개선된 멀티탭 제작</li>
    </ul>
</div>

<div class="image-wrapper">
    <div class="image-container" style="width:100%">
        <div class="image-container__header">
            <h3>이미지</h3>
        </div>
        <div class="image-container__image">
            <div class="slide">
                <img src="./reimg/fire.webp">
            </div>
            <div class="slide fade">
                <img src="./reimg/ne.webp">
            </div>
        </div>
    </div>
</div>

</div>

<div class="progress">
  <div class="bar" style="--start-progress: 2;">
</div>

---

<div class="spe-star"></div>

<div class="header slowup">
🚀 <span class="sub1"> 서론 </span> 🔹 <strong>기존 제품 분석</strong>
</div>

<div class="content slowup" style="--img-flex: 0; --text-flex: 1">

 <div class="text slowup" style="--order: 2;">
 
<h3 class="slowup" style="--order: 2.2;"> 기존 제품 비교 </h3>

<div class="s-table slowup" style="--order: 2.7;">
    <img src="./reimg/energymeter.webp">
    <span class="s-frac">전기 요금 측정기</span>
    <span class="s-point"><strong>콘센트</strong>→<strong>측정기</strong>→<strong>기기</strong>순 연결, 1구 사용, 리드선 X</span>
</div>

<div class="s-table slowup" style="--order: 2.9;">
    <img src="./reimg/wattmeter.webp">
    <span class="s-frac">전력계 멀티탭</span>
    <span class="s-point">전력 출력, <strong>IoT</strong> 및 <strong>Wifi 통신</strong>으로 원격 계측 및 제어 가능</span>
</div>

<div class="s-table slowup" style="--order: 3.1;">
    <img src="./reimg/breaker.webp">
    <span class="s-frac">차단기 멀티탭</span>
    <span class="s-point"><strong>과전류</strong> 발생 시 멀티탭 <strong>전체 차단</strong></span>
</div>

<div class="s-table slowup" style="--order: 3.3;">
    <img src="./reimg/indiv.webp">
    <span class="s-frac">개별전원 멀티탭</span>
    <span class="s-point">코드 연결 후 미 사용 시 <strong>개별 차단</strong> 가능</span>
</div>

 </div>
</div>

<div class="progress">
  <div class="bar" style="--start-progress: 3;">
</div>

---

<div class="spe-star"></div>

<style scoped>
.s-frac {
    flex: 0.2;
}

.s-point {
    flex: 0.7;
    font-size: 0.9rem;
}

h6 {
  margin-left: 0;
  display: flex;
  align-items: center;
  justify-content: flex-start;
  gap: 0.1rem; /* 별과 글자 간격 */

}
</style>

<div class="header slowup">
🚀 <span class="sub1"> 서론 </span> 🔹 <strong>기존 제품 분석</strong>
</div>

<div class="content slowup" style="--img-flex: 0; --text-flex: 1">

 <div class="text slowup" style="--order: 2;">
 
<h3 class="slowup" style="--order: 2.2;"> 개선 가능한 부분 </h3>

<div class="s-table slowup" style="--order: 2.7;">
    <span class="s-frac">전기 요금 측정기</span>
    <span class="s-point"><span class="red">멀티탭 내장</span> 시, <strong>위치 제한 해소</strong>  및  <strong>편의성 향상</strong> 가능</span>
</div>

<div class="s-table slowup" style="--order: 2.9;">
    <span class="s-frac">전력계 멀티탭</span>
    <span class="s-point">비싼<span class="red">IoT</span> 및 <span class="red">WIFI</span> 모듈 제외<br><strong>Display</strong>, <strong>LED</strong>, <strong>Buzzer</strong>로 대체해 <strong>가성비</strong>, <strong>시인성</strong> 향상</span>
</div>

<div class="s-table slowup" style="--order: 3.1;">
    <span class="s-frac">차단기 멀티탭</span>
    <span class="s-point"><span class="red">과전류</span> 시 전체가 아닌<br><strong>개별 차단</strong>으로 <strong>사용 편의성</strong> 향상</span>
</div>

<div class="s-table slowup" style="--order: 3.3;">
    <span class="s-frac">개별전원 멀티탭</span>
    <span class="s-point"><span class="red">스위치</span> 대신 버튼으로 변경<br>코드를 빼면 <strong>자동 제어</strong>를 해 <strong>편의성</strong>, <strong>안전성</strong> 향상</span>
</div>

<h6 class="slowup" style="--order: 3.5;"> <span class="star">⭐</span><span class="red">편의성</span> 및 <span class="red">안전성 </span> 위주의 <strong>안전 시스템</strong>을 갖춘 멀티탭을 목표</h6>

 </div>
</div>

<div class="progress">
  <div class="bar" style="--start-progress: 4;">
</div>

---

<div class="spe-star opac"></div>
<div class="sky stitle">
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
</div>

<div class="half">
<div class="img slowup" style="--order: 0; flex: 0.5">
<img src="./reimg/main.webp" style="width: 90%;">
</div>

<div class="text slowup" style="--order: 1;">
    <h1 class="sub2 slowup"  style="--order: 1.2;"><span class="sub2"> 설계 및 구현 </span></h1>
    <ul>
        <li class="slowup" style="--order: 1.7;">소프트웨어 및 하드웨어</li>
        <li class="slowup" style="--order: 2.2;">주요 기능</li>
    </ul>
</div>
</div>

<div class="progress">
  <div class="bar" style="--start-progress: 5;">
</div>

---

<div class="spe-star"></div>

<div class="header slowup">
🛠️ <span class="sub2"> 설계 및 구현 </span> 🔹 <strong>소프트웨어 및 <span class="red">하드웨어</span></strong>
</div>

<div class="content slowup" style="--text-flex: 0.5">

<div class="text slowup" style="--order: 2;">
    <h3 class="slowup" style="--order: 2.2;">하드웨어 구성</h3>
    <ul>
        <li class="slowup" style="--order: 2.7;">🕹️ <span class="red">아두이노</span> <sub>ATMega 2560</sub></li>
        <li class="slowup" style="--order: 2.9;">🕹️ <span class="red">릴레이</span> <sub>SRD-05VDC-SL-C</sub></li>
        <li class="slowup" style="--order: 3.1;">⚙️ <span class="blue">전압 센서</span> <sub>ZMPT101B</sub></li>
        <li class="slowup" style="--order: 3.3;">⚙️ <span class="blue">전류 센서</span> <sub>ACS712 20A</sub></li>
        <li class="slowup" style="--order: 3.5;">⚙️ <span class="blue">감압 센서</span> <sub>FSR</sub></li>
        <li class="slowup" style="--order: 3.7;">📡 <span class="green">블루투스 모듈</span> <sub>HM-10</sub></li>
        <li class="slowup" style="--order: 3.9;">📡 <span class="green">디스플레이</span> <sub>TFT LCD ST7735</sub></li>
        <li class="slowup" style="--order: 4.1;">📡 <span class="green">LED, 부저</span> <sub>RGB, 압전 부저</sub></li>
    </ul>
</div>

<div class="image-wrapper">
    <div class="image-container">
        <div class="image-container__header">
            <h3>내부 구조</h3>
        </div>
        <div class="image-container__image">
            <img src="./reimg/inside.webp">
        </div>
    </div>
</div>

</div>

<div class="progress">
  <div class="bar" style="--start-progress: 6;">
</div>

---

<div class="spe-star"></div>

<div class="header slowup">
🛠️ <span class="sub2"> 설계 및 구현 </span> 🔹 <strong><span class="green">소프트웨어</span> 및 하드웨어</strong>
</div>

<div class="content slowup" style="--text-flex: 0.5">

<div class="text slowup" style="--order: 2;">
    <h3 class="slowup" style="--order: 2.2;">소프트웨어 구성</h3>
    <ul>
        <li class="slowup" style="--order: 2.7;">⚙️ <span class="blue">센서 데이터 수집 및 샘플링</span><br><h5>Analog > Digital 변환</h5></li>
        <li class="slowup" style="--order: 2.9;">⚙️ <span class="blue">전력, 전압, 전류 계산</span><br><h5>Digital값 보정 후 반환</h5></li>
        <li class="slowup" style="--order: 3.1;">🕹️ <span class="red">데이터 수집 결과 분석</span></li>
        <li class="slowup" style="--order: 3.3;">🕹️ <span class="red">과전류 개별 차단 및 경고 시스템</span><br><h5>부저&LED 경고</h5></li>
        <li class="slowup" style="--order: 3.5;">📡 <span class="green">디스플레이 및 블루투스 출력</span><br><h5>디스플레이&웹 출력</h5></li>
    </ul>
</div>

<div class="image-wrapper">
    <div class="image-container">
        <div class="image-container__header">
            <h3>알고리즘 흐름도</h3>
        </div>
        <div class="image-container__image">
            <img src="./reimg/algorithm.webp">
        </div>
    </div>
</div>

</div>

<div class="progress">
  <div class="bar" style="--start-progress: 7;">
</div>

---

<div class="spe-star"></div>

<div class="header slowup">
🛠️ <span class="sub2"> 설계 및 구현 </span> 🔹 <strong>주요 기능</strong>
</div>

<div class="content slowup" style="--text-flex: 0.6">

<div class="text slowup" style="--order: 2;">

<h3 class="slowup" style="--order: 2.2"> <span style="color: #fff;">💻</span> <span class="blue">전력 모니터링 기능</span></h3>

<h4 class="slowup" style="--order: 2.7">디스플레이</h4>
<ul>
    <li class="slowup" style="--order: 2.9">1초마다 전력, 전압, 전류 정보 제공</li>
    <li class="slowup" style="--order: 3.1">화면보호기 기능 [10s]</li>
</ul>

<h4 class="slowup" style="--order: 3.6">웹페이지</h4>
<ul>
    <li class="slowup" style="--order: 3.8">예측 일간, 주간, 월간 소비 전력량 제공</li>
    <li class="slowup" style="--order: 3.8">원격 제어 가능</li>
</ul>

</div>

<div class="image-wrapper">
    <div class="image-container" style="width: 90%">
        <div class="image-container__header">
            <h3>전력 모니터링</h3>
        </div>
        <div class="image-container__image">
            <div class="slide">
                <img src="./reimg/web.webp">
            </div>
            <div class="slide fade">
                <img src="./reimg/display.webp">
            </div>
        </div>
    </div>
</div>

</div>

<div class="progress">
  <div class="bar" style="--start-progress: 8;">
</div>

---

<div class="spe-star"></div>

<div class="header slowup">
🛠️ <span class="sub2"> 설계 및 구현 </span> 🔹 <strong>주요 기능</strong>
</div>

<div class="content slowup" style="--text-flex: 0.6">

<div class="text slowup" style="--order: 2;">

<h3 class="slowup" style="--order: 2.2"> <span style="color: #fff;">⚡ <span class="red">과전류 개별 차단 및 경고 기능</span></h3>

<h4 class="slowup" style="--order: 2.7">과전류 차단</h4>
<ul>
    <li class="slowup" style="--order: 2.9">총 15A, 개별 8A 허용 전류 [240ms]</li>
    <li class="slowup" style="--order: 3.1">콘센트 당 2개의 릴레이로 개별 차단</li>
</ul>

<h4 class="slowup" style="--order: 3.6">경고</h4>
<ul>
    <li class="slowup" style="--order: 3.8">이상 시 부저 동작</li>
    <li class="slowup" style="--order: 4"><span class="red">이상</span>/<span class="green">정상</span>/<span class="blue">꺼짐</span> 시 <span class="red">R</span>/<span class="green">G</span>/<span class="blue">B</span> LED 점등</li>
</ul>

</div>

<div class="image-wrapper">
    <div class="image-container">
        <div class="image-container__header">
            <h3>과전류 차단</h3>
        </div>
        <div class="image-container__image">
            <img src="./reimg/ovr.gif">
        </div>
    </div>
</div>

</div>

<div class="progress">
  <div class="bar" style="--start-progress: 9;">
</div>

---

<div class="spe-star"></div>

<div class="header slowup">
🛠️ <span class="sub2"> 설계 및 구현 </span> 🔹 <strong>주요 기능</strong>
</div>

<div class="content slowup" style="--text-flex: 0.6">

<div class="text slowup" style="--order: 2;">

<h3 class="slowup" style="--order: 2.2"> <span style="color: #fff;">🔌</span> <span class="green">코드 감응형 차단 기능</span></h3>

<h4 class="slowup" style="--order: 2.7">코드 감응</h4>
<ul>
    <li class="slowup" style="--order: 2.9">FSR 센서 기반</li>
    <li class="slowup" style="--order: 3.1">코드가 삽입된 경우 <span class="green">ON</span>/<span class="red">OFF</span> 가능</li>
    <li class="slowup" style="--order: 3.3">코드가 삽입이 안된 경우 <span class="red">OFF</span>만 가능</li>
</ul>

</div>

<div class="image-wrapper">
    <div class="image-container" style="width:90%">
        <div class="image-container__header">
            <h3>코드 감응형 차단</h3>
        </div>
        <div class="image-container__image">
            <img src="./reimg/fsr2.webp">
            <img src="./reimg/fsr1.webp">
        </div>
    </div>
</div>

</div>

<div class="progress">
  <div class="bar" style="--start-progress: 10;">
</div>

---

<div class="spe-star opac"></div>
<div class="sky stitle">
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
</div>

<div class="half">
<div class="img slowup" style="--order: 0; flex: 0.5">
<img src="./reimg/main.webp" style="width: 90%;">
</div>

<div class="text slowup" style="--order: 1;">
    <h1 class="sub3 slowup" style="--order: 1.2;"><span class="sub3"> 실험 및 결과 </span></h1>
    <ul>
        <li class="slowup" style="--order: 2.2;">실험 분석 및 해결 방안</li>
    </ul>
</div>
</div>

<div class="progress">
  <div class="bar" style="--start-progress: 11;">
</div>

---

<div class="spe-star"></div>

<div class="header slowup">
🧪 <span class="sub3"> 실험 및 결과 </span> 🔹 <strong><span class="green">실험 분석</span> 및 해결 방안</strong>
</div>

<div class="content slowup" style="--text-flex: 0.5">

<div class="text slowup" style="--order: 2;">

<h3 class="slowup" style="--order: 2.2"> <span style="color: #fff;">🚫 <span class="red">릴레이 차단 테스트</span></h3>

<h4 class="slowup" style="--order: 2.7">실험 목적</h4>
<ul>
    <li class="slowup" style="--order: 2.9">220V 제어 여부 확인</li>
    <li class="slowup" style="--order: 3.1">동작 확인</li>
</ul>

<h4 class="slowup" style="--order: 3.6">실험 결과</h4>
<ul>
    <li class="slowup" style="--order: 3.8"><span style="color: #fff;">✅ 220V 제어 <span class="green">성공</span></li>
    <li class="slowup" style="--order: 4"><span style="color: #fff;">❌ <span class="red">아두이노 OFF</span></li>
</ul>

</div>

<div class="image-wrapper">
    <div class="image-container" style="width:80%;">
        <div class="image-container__header">
            <h3>실험 과정&데이터</h3>
        </div>
        <div class="image-container__image">
            <div class="slide">
                <img src="./reimg/test1.webp">
            </div>
            <div class="slide fade">
                <img src="./reimg/relay.webp">
            </div>
        </div>
    </div>
</div>

</div>

<div class="progress">
  <div class="bar" style="--start-progress: 12;">
</div>

---

<div class="spe-star"></div>

<div class="header slowup">
🧪 <span class="sub3"> 실험 및 결과 </span> 🔹 <strong>실험 분석 및 <span class="red">해결 방안</span></strong>
</div>

<div class="content slowup" style="--text-flex: 0.5">

<div class="text slowup" style="--order: 2;">

<h3 class="slowup" style="--order: 2.2"> <span style="color: #fff;">🚫 <span class="red">릴레이 차단 테스트</span></h3>

<h4 class="slowup" style="--order: 2.7"><strong>아두이노 OFF</strong> 원인 분석</h4>
<ul>
    <li class="slowup" style="--order: 2.9">릴레이 제어 시 서지 전류 유입</li>
    <li class="slowup" style="--order: 3.1">서지 전류로 인해 아두이노 OFF</li>
</ul>

<h4 class="slowup" style="--order: 3.6">해결 방안</h4>
<ul>
    <li class="slowup" style="--order: 3.8"><span style="color: #fff;">서지 전류를 위해 <span class="green">RC 스너버</span> 설치</span></li>
    <li class="slowup" style="--order: 4"><span style="color: #fff;">RC 스너버 설치 후 문제 해결</span></li>
</ul>

</div>

<div class="image-wrapper">
    <div class="image-container" style="width:80%;">
        <div class="image-container__header">
            <h3>서지 데이터&RC 스너버</h3>
        </div>
        <div class="image-container__image">
            <div class="slide">
                <img src="./reimg/surge.webp">
            </div>
            <div class="slide fade">
                <img src="./reimg/surge2.webp">
            </div>
        </div>
    </div>
</div>

</div>

<div class="progress">
  <div class="bar" style="--start-progress: 13;">
</div>

---

<div class="spe-star"></div>

<div class="header slowup">
🧪 <span class="sub3"> 실험 및 결과 </span> 🔹 <strong><span class="green">실험 분석</span> 및 해결 방안</strong>
</div>

<div class="content slowup" style="--text-flex: 0.5">

<div class="text slowup" style="--order: 2;">

<h3 class="slowup" style="--order: 2.2"> <span style="color: #fff;">⚡ <span class="blue">전압, 전류 측정 테스트</span></span></h3>

<h4 class="slowup" style="--order: 2.7">실험 목적</h4>
<ul>
    <li class="slowup" style="--order: 2.9">전압 측정값 정확도 확인</li>
    <li class="slowup" style="--order: 3.1">기타 문제사항 확인</li>
</ul>

<h4 class="slowup" style="--order: 3.6">실험 결과</h4>
<ul>
    <li class="slowup" style="--order: 3.8"><span style="color: #fff;">✅ 측정 <span class="green">성공</span></span></li>
    <li class="slowup" style="--order: 4"><span style="color: #fff;">⚠️ 2~5V <span class="red">오차 발생</span></span></li>
</ul>

</div>

<div class="image-wrapper">
    <div class="image-container" >
        <div class="image-container__header">
            <h3>[15EA] 전압 측정 데이터</h3>
        </div>
        <div class="image-container__image">
            <img src="./reimg/voltage.webp">
        </div>
    </div>
</div>

</div>

<div class="progress">
  <div class="bar" style="--start-progress: 14;">
</div>

---

<div class="spe-star"></div>

<div class="header slowup">
🧪 <span class="sub3"> 실험 및 결과 </span> 🔹 <strong><span class="green">실험 분석</span> 및 해결 방안</strong>
</div>

<div class="content slowup" style="--text-flex: 0.5">

<div class="text slowup" style="--order: 2;">

<h3 class="slowup" style="--order: 2.2"> <span style="color: #fff;">⚡ <span class="blue">전압, 전류 측정 테스트</span></span></h3>

<h4 class="slowup" style="--order: 2.7">실험 목적</h4>
<ul>
    <li class="slowup" style="--order: 2.9">전류 측정값 정확도 확인</li>
    <li class="slowup" style="--order: 3.1">기타 문제사항 확인</li>
</ul>

<h4 class="slowup" style="--order: 3.6">실험 결과</h4>
<ul>
    <li class="slowup" style="--order: 3.8"><span style="color: #fff;">✅ 측정 <span class="green">성공</span></span></li>
    <li class="slowup" style="--order: 4"><span style="color: #fff;">⚠️ 100~180mA <span class="red">오차 발생</span></span></li>
</ul>

</div>

<div class="image-wrapper">
    <div class="image-container" >
        <div class="image-container__header">
            <h3>[10EA] 전류 측정 데이터</h3>
        </div>
        <div class="image-container__image">
            <img src="./reimg/current.webp">
        </div>
    </div>
</div>

</div>

<div class="progress">
  <div class="bar" style="--start-progress: 15;">
</div>

---

<div class="spe-star"></div>

<div class="header slowup">
🧪 <span class="sub3"> 실험 및 결과 </span> 🔹 <strong>실험 분석 및 <span class="red">해결 방안</span></strong>
</div>

<div class="content slowup" style="--text-flex: 0.5">

<div class="text slowup" style="--order: 2;">

<h3 class="slowup" style="--order: 2.2"> <span style="color: #fff;">⚡ <span class="blue">전압, 전류 측정 테스트</span></span></h3>

<h4 class="slowup" style="--order: 2.7"><strong>오차</strong> 원인 분석</h4>
<ul>
    <li class="slowup" style="--order: 2.9">Analog > Digital 변환식 문제</li>
    <li class="slowup" style="--order: 3.1">OFFSET</li>
</ul>

<h4 class="slowup" style="--order: 3.6">해결 방안</h4>
<ul>
    <li class="slowup" style="--order: 3.8"><span style="color: #fff;">OFFSET <span class="green">보정</span> 추가</span></li>
    <li class="slowup" style="--order: 4"><span style="color: #fff;">구간 별 <span class="green">보정</span> 및 <span class="green">샘플링</span> 추가</span></li>
</ul>

</div>

<div class="image-wrapper">
    <div class="image-container" >
        <div class="image-container__header">
            <h3>OFFSET</h3>
        </div>
        <div class="image-container__image">
            <img src="./reimg/offset.gif">
        </div>
    </div>
</div>

</div>

<div class="progress">
  <div class="bar" style="--start-progress: 16;">
</div>

---

<div class="spe-star"></div>

<div class="header slowup">
🧪 <span class="sub3"> 실험 및 결과 </span> 🔹 <strong><span class="green">실험 분석</span> 및 해결 방안</strong>
</div>

<div class="content slowup" style="--text-flex: 0.5">

<div class="text slowup" style="--order: 2;">

<h3 class="slowup" style="--order: 2.2"> <span style="color: #fff;">⚡ <span class="red">과전류 감지 및 차단 테스트</span></span></h3>

<h4 class="slowup" style="--order: 2.7">실험 목적</h4>
<ul>
    <li class="slowup" style="--order: 2.9">과전류 차단 여부 확인</li>
    <li class="slowup" style="--order: 3.1">소요 시간 확인</li>
</ul>

<h4 class="slowup" style="--order: 3.6">실험 결과</h4>
<ul>
    <li class="slowup" style="--order: 3.8"><span style="color: #fff;">✅ 과전류 차단 <span class="green">성공</span></span></li>
    <li class="slowup" style="--order: 4"><span style="color: #fff;">❌ 차단 시간 <span class="red">[380ms]</span></span></li>
</ul>

</div>

<div class="image-wrapper">
    <div class="image-container" style="width:100%;">
        <div class="image-container__header">
            <h3>과전류 실험 과정</h3>
        </div>
        <div class="image-container__image">
            <div class="slide">
                <img src="./reimg/ovr1.webp">
            </div>
            <div class="slide fade">
                <img src="./reimg/ovr2.webp">
            </div>
        </div>
    </div>
</div>

</div>

</div>

<div class="progress">
  <div class="bar" style="--start-progress: 17;">
</div>

---

<div class="spe-star"></div>

<div class="header slowup">
🧪 <span class="sub3"> 실험 및 결과 </span> 🔹 <strong>실험 분석 및 <span class="red">해결 방안</span></strong>
</div>

<div class="content slowup" style="--text-flex: 0.5">

<div class="text slowup" style="--order: 2;">

<h3 class="slowup" style="--order: 2.2"> <span style="color: #fff;">⚡ <span class="red">과전류 감지 및 차단 테스트</span></span></h3>

<h4 class="slowup" style="--order: 2.7"><strong>차단 지연</strong> 원인 분석</h4>
<ul>
    <li class="slowup" style="--order: 2.9">싱글 스레드 기반 MCU</li>
    <li class="slowup" style="--order: 3.1">디스플레이 출력 시 지연 발생</li>
</ul>

<h4 class="slowup" style="--order: 3.6">해결 방안</h4>
<ul>
    <li class="slowup" style="--order: 3.8"><span style="color: #fff;"><span class="green">화면보호기</span> 도입</span></li>
    <li class="slowup" style="--order: 4"><span style="color: #fff;">이전과 동일한 값<br>출력 안하게 코드 최적화</span></li>
</ul>

</div>

<div class="image-wrapper">
    <div class="image-container">
        <div class="image-container__header">
            <h3>코드 최적화 전&후</h3>
        </div>
        <div class="image-container__image">
            <img src="./reimg/predisplay.gif">
            <img src="./reimg/display.gif">
        </div>
    </div>
</div>

</div>

<div class="progress">
  <div class="bar" style="--start-progress: 18;">
</div>

---

<div class="spe-star"></div>

<div class="header slowup">
🧪 <span class="sub3"> 실험 및 결과 </span> 🔹 <strong><span class="green">실험 분석</span> 및 해결 방안</strong>
</div>

<div class="content slowup" style="--text-flex: 0.5">

<div class="text slowup" style="--order: 2;">

<h3 class="slowup" style="--order: 2.2"> <span style="color: #fff;">🚨 <span class="blue">경고 시스템 구현 테스트</span></span></h3>

<h4 class="slowup" style="--order: 2.7">실험 목적</h4>
<ul>
    <li class="slowup" style="--order: 2.9">LED 및 부저 동작 확인</li>
    <li class="slowup" style="--order: 3.1">기타 문제사항 확인</li>
</ul>

<h4 class="slowup" style="--order: 3.6">실험 결과</h4>
<ul>
    <li class="slowup" style="--order: 3.8"><span style="color: #fff;">✅ 동작 <span class="green">성공</span></span></li>
    <li class="slowup" style="--order: 4"><span style="color: #fff;">❌ 센서 <span class="red">노이즈 발생</span></span></li>
</ul>

</div>

<div class="image-wrapper">
    <div class="image-container">
        <div class="image-container__header">
            <h3>실험 과정</h3>
        </div>
        <div class="image-container__image">
            <img src="./reimg/alert.gif">
        </div>
    </div>
</div>

</div>

<div class="progress">
  <div class="bar" style="--start-progress: 19;">
</div>

---

<div class="spe-star"></div>

<div class="header slowup">
🧪 <span class="sub3"> 실험 및 결과 </span> 🔹 <strong>실험 분석 및 <span class="red">해결 방안</span></strong>
</div>

<div class="content slowup" style="--text-flex: 0.5">

<div class="text slowup" style="--order: 2;">

<h3 class="slowup" style="--order: 2.2"> <span style="color: #fff;">🚨 <span class="blue">경고 시스템 구현 테스트</span></span></h3>

<h4 class="slowup" style="--order: 2.7">센서 <strong>노이즈</strong> 원인 분석</h4>
<ul>
    <li class="slowup" style="--order: 2.9">부저 동작 시 노이즈 발생</li>
    <li class="slowup" style="--order: 3.1">부저로 인한 전압 변동</li>
</ul>

<h4 class="slowup" style="--order: 3.6">해결 방안</h4>
<ul>
    <li class="slowup" style="--order: 3.8"><span style="color: #fff;">부저 동작 시 <span class="green">이전 데이터</span> 호출</span></li>
    <li class="slowup" style="--order: 4"><span style="color: #fff;">소프트웨어적 해결</span></li>
</ul>

</div>

<div class="image-wrapper">
    <div class="image-container">
        <div class="image-container__header">
            <h3>노이즈 해결 전&후</h3>
        </div>
        <div class="image-container__image col">
            <img src="./reimg/buzzer1.gif">
            <img src="./reimg/buzzer2.gif">
        </div>
    </div>
</div>

</div>

<div class="progress">
  <div class="bar" style="--start-progress: 20;">
</div>

---

<div class="spe-star opac"></div>
<div class="sky stitle">
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
</div>

<div class="half">
<div class="img slowup" style="--order: 0; flex: 0.5">
<img src="./reimg/main.webp" style="width: 90%;">
</div>

<div class="text slowup" style="--order: 1;">
    <h1 class="sub4 slowup"  style="--order: 1.2;"><span class="sub4"> 고찰 및 결론 </span></h1>
    <ul>
        <li class="slowup" style="--order: 1.7;">연구 결과 분석</li>
        <li class="slowup" style="--order: 2.2;">한계점 및 개선 방안</li>
        <li class="slowup" style="--order: 2.7;">결론</li>
    </ul>
</div>
</div>

<div class="progress">
  <div class="bar" style="--start-progress: 21;">
</div>

---

<div class="spe-star"></div>

<div class="header slowup">
🔍 <span class="sub4"> 고찰 및 결론 </span> 🔹 <strong>연구 결과 분석</strong>
</div>

<div class="content slowup" style="--text-flex: 0.5">

<div class="text slowup" style="--order: 2;">

<h3 class="slowup" style="--order: 2.2"> <span style="color: #fff;">💻</span> <span class="blue">전력 모니터링 기능</span></h3>

<h4 class="slowup" style="--order: 2.7">실시간 데이터 제공</h4>
<ul>
    <li class="slowup" style="--order: 2.9">디스플레이를 통해
    전력, 전압, 전류 <br>소비량 실시간 시각화</li>
    <li class="slowup" style="--order: 3.1">모바일 및 PC 또한 모니터링 가능</li>
</ul>

<h4 class="slowup" style="--order: 3.6">에너지 사용 관리 기여</h4>
<ul>
    <li class="slowup" style="--order: 3.8">알고리즘으로 전력량 예측 가능</li>
</ul>

</div>

<div class="image-wrapper">
    <div class="image-container" style="width: 100%">
        <div class="image-container__header">
            <h3>전력 모니터링</h3>
        </div>
        <div class="image-container__image">
            <div class="slide">
                <img src="./reimg/web.webp">
            </div>
            <div class="slide fade">
                <img src="./reimg/display.webp">
            </div>
        </div>
    </div>
</div>

</div>

<div class="progress">
  <div class="bar" style="--start-progress: 22;">
</div>

---

<div class="spe-star"></div>

<div class="header slowup">
🔍 <span class="sub4"> 고찰 및 결론 </span> 🔹 <strong>연구 결과 분석</strong>
</div>

<div class="content slowup" style="--text-flex: 0.5">

<div class="text slowup" style="--order: 2;">

<h3 class="slowup" style="--order: 2.2"> <span style="color: #fff;">⚡</span> <span class="red">과전류 개별 차단 및 경고 기능</span></h3>

<h4 class="slowup" style="--order: 2.7">편의성 보장</h4>
<ul>
    <li class="slowup" style="--order: 2.9">총 15A, 개별 8A의 허용 전류</li>
    <li class="slowup" style="--order: 3.1">과전류가 발생한 콘센트만 차단하여 <br>다른 기기 동작에는 영향 최소화</li>
</ul>
<h4 class="slowup" style="--order: 3.6">사고 대응성 강화</h4>
<ul>
    <li class="slowup" style="--order: 3.8">LED를 통한 시각적 경고</li>
    <li class="slowup" style="--order: 4">부저를 통한 청각적 경고</li>
</ul>

</div>

<div class="image-wrapper">
    <div class="image-container">
        <div class="image-container__header">
            <h3>과전류 차단</h3>
        </div>
        <div class="image-container__image">
            <img src="./reimg/ovr.gif">
        </div>
    </div>
</div>

</div>

<div class="progress">
  <div class="bar" style="--start-progress: 23;">
</div>

---

<div class="spe-star"></div>

<div class="header slowup">
🔍 <span class="sub4"> 고찰 및 결론 </span> 🔹 <strong>연구 결과 분석</strong>
</div>

<div class="content slowup" style="--text-flex: 0.5">

<div class="text slowup" style="--order: 2;">

<h3 class="slowup" style="--order: 2.2"> <span style="color: #fff;">🔌</span>  <span class="green">코드 감응형 차단 기능</span></h3>

<h4 class="slowup" style="--order: 2.7">감전 사고 예방</h4>
<ul>
    <li class="slowup" style="--order: 2.9">플러그 미삽입 시 전류 차단으로<br>감전 사고 예방</li>
</ul>

<h4 class="slowup" style="--order: 3.4">어린이 안전 강화</h4>
<ul>
    <li class="slowup" style="--order: 3.6">콘센트에 이물질을 삽입해도<br>전류가 차단된 상태 유지</li>
</ul>

</div>

<div class="image-wrapper">
    <div class="image-container">
        <div class="image-container__header">
            <h3>어린이 감전사고 기사</h3>
        </div>
        <div class="image-container__image">
            <img src="./reimg/news.webp">
        </div>
    </div>
</div>

</div>

<div class="progress">
  <div class="bar" style="--start-progress: 24;">
</div>

---

<div class="spe-star"></div>

<style scoped>
@keyframes fadeEffect {
    0% {
        opacity: 0;
    }
    8.33% {
        opacity: 1;
    } /* 1초 동안 보이게 설정 (12s / 4 = 3s / 3단계) */
    25% {
        opacity: 1;
    }
    33.33% {
        opacity: 0;
    }
    100% {
        opacity: 0;
    }
}

.slide {
    animation: fadeEffect 20s infinite;
}

.slide:nth-child(1) {
    animation-delay: 0s;
}
.slide:nth-child(2) {
    animation-delay: 4s;
}
.slide:nth-child(3) {
    animation-delay: 8s;
}
.slide:nth-child(4) {
    animation-delay: 12s;
}
.slide:nth-child(5) {
    animation-delay: 16s;
}

li {
    font-size: 0.9rem;
}
</style>

<div class="header slowup">
🔍 <span class="sub4"> 고찰 및 결론 </span> 🔹 <strong>한계점 및 개선 방안</strong>
</div>

<div class="content slowup" style="--text-flex: 0.5">

<div class="text slowup" style="--order: 2;">

<h4 class="slowup" style="--order: 2.7">하드웨어 크기</h4>
<ul>
    <li class="slowup" style="--order: 2.9">⚠️ 2구 멀티탭이지만 <span class="red">30cm의 큰 크기</li>
    <li class="slowup" style="--order: 3.1">✨ <span class="green">부품 집적도 개선 & 벽면 매립 </li>
</ul>
<h4 class="slowup" style="--order: 3.6">센서 측정 오차</h4>
<ul>
    <li class="slowup" style="--order: 3.8">⚠️ <span class="red">전류 100mA & 전압 1~3%</span> 오차 발생</li>
    <li class="slowup" style="--order: 4">✨ <span class="green">센서 보정 절차 강화 </li>
</ul>

<h4 class="slowup" style="--order: 4.5">차단 시간</h4>
<ul>
    <li class="slowup" style="--order: 4.7">⚠️ 디스플레이 출력 시 <span class="red">차단 시간 [300ms]</li>
    <li class="slowup" style="--order: 4.9">✨ <span class="green">MCU 교체 및 멀티 스레딩 도입 </li>
</ul>

</div>

<div class="image-wrapper">
    <div class="image-container" style="width: 100%">
        <div class="image-container__header">
            <h3>이미지</h3>
        </div>
        <div class="image-container__image">
            <div class="slide">
                <img src="./reimg/outside.webp">
            </div>
            <div class="slide">
                <img src="./reimg/inside.webp">
            </div>
            <div class="slide fade">
                <img src="./reimg/voltage.webp">
            </div>
            <div class="slide fade">
                <img src="./reimg/current.webp">
            </div>
            <div class="slide fade">
                <img src="./reimg/log.webp">
            </div>
        </div>
    </div>
</div>

</div>

<div class="progress">
  <div class="bar" style="--start-progress: 25;">
</div>

---

<div class="spe-star"></div>

<div class="header slowup">
🔍 <span class="sub4"> 고찰 및 결론 </span> 🔹 <strong>결론</strong>
</div>

<div class="content slowup">
    <div class="text slowup" style="--order: 2;">
        <h2 class="slowup" style="--order: 2.2;"><span style="color: #fff;">📚<strong> 주요 기능</strong></h2>
        <ul>
            <li class="slowup" style="--order: 2.4;">💻<span class="blue">전력 모니터링 기능</span><br>
            <h5>소비 전력 디스플레이 및 웹 제공<br>효율적 전기 사용 가이드</h5></li>
            <li class="slowup" style="--order: 2.6;">⚡<span class="red">과전류 개별 차단 및 경고 기능</span><br>
            <h5>개별 차단 <br>시/청각적 경고로 즉각 대응</h5></li>
            <li class="slowup" style="--order: 2.8;">🔌<span class="green">코드 감응형 차단 기능</span><br>
            <h5>코드 삽입 시 전류 ON<br>감전 사고 예방</h5></li>
        </ul>
    </div>
    <div class="text slowup" style="--order: 3.3;">
        <h2 class="slowup" style="--order: 3.5;"><span style="color: #fff;">📚 기대 효과</h2>
        <ul>
            <li class="slowup" style="--order: 3.7;">감전 사고 예방 및 편의성 증대</li>
            <li class="slowup" style="--order: 3.9;">가정&사무실 전기 사용 환경 개선</li>
        </ul>
        <h2 class="slowup" style="--order: 4.1;"><span style="color: #fff;">📚 향후 개선 방향</h2>
        <ul>
            <li class="slowup" style="--order: 4.3;">집적도 개선으로 소형화</li>
            <li class="slowup" style="--order: 4.5;">전압&전류 센서 정밀도 향상</li>
            <li class="slowup" style="--order: 4.7;">벽면 매입형 콘센트로 전환 고려</li>
            <li class="slowup" style="--order: 4.9;">멀티스레드 처리로 지연 시간 개선</li>
        </ul>
    </div>

</div>

<div class="progress">
  <div class="bar" style="--start-progress: 26;">
</div>

---

<div class="spe-star opac"></div>
<div class="sky">
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
        <div class="meteor"></div>
</div>

<div class="end">감사합니다</div>

<div class="progress">
  <div class="bar" style="--start-progress: 27;">
</div>
