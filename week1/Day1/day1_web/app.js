"use strict";

// 계산은 브라우저에서 수행합니다. 서버 호출과 외부 라이브러리가 없습니다.
function readInteger(value, label) {
  const text = String(value).trim();
  if (!/^[+-]?\d+$/.test(text) || !Number.isSafeInteger(Number(text))) {
    throw new Error(`${label}: 정확히 표현 가능한 정수를 입력하세요.`);
  }
  return Number(text);
}

function addNumbers(a, b) {
  const sum = a + b;
  if (!Number.isSafeInteger(sum)) throw new Error("계산 결과가 너무 큽니다. 더 작은 숫자를 입력하세요.");
  return sum;
}

function evenNumbers(values) { return values.filter(value => value % 2 === 0); }
function multiplicationRows() {
  return Array.from({ length: 9 }, (_, row) =>
    Array.from({ length: 8 }, (_, col) => `${col + 2} × ${row + 1} = ${(col + 2) * (row + 1)}`));
}
function guessHint(guess, answer) {
  return guess === answer ? "정답입니다." : guess > answer ? "컴퓨터보다 큽니다." : "컴퓨터보다 작습니다.";
}

const lessons = [
  {
    "title": "변수와 연산",
    "description": "두 숫자를 더해 변수와 산술 연산의 결과를 확인합니다.",
    "challenge": "뺄셈·곱셈·나눗셈을 추가하려면 app.js의 계산 로직을 수정해 보세요.",
    "code": "number1 = 100\nnumber2 = 200\nprint(\"number1 + number2 = \", number1 + number2)"
  },
  {
    "title": "합격 판정",
    "description": "입력한 점수가 60점 이상이면 합격, 그 외에는 불합격입니다.",
    "challenge": "59점과 60점을 비교하세요. 합격 기준을 70점으로 바꾸어 보세요.",
    "code": "score = int(input(\"점수를 입력하세요 : \"))\nif score >= 60:\n    print(\"합격\")\nelse:\n    print(\"불합격\")"
  },
  {
    "title": "리스트와 짝수",
    "description": "숫자 5개를 리스트에 저장하고, 2로 나눈 나머지가 0인 숫자만 골라냅니다.",
    "challenge": "음수와 0도 넣어 보세요. 홀수를 고르도록 조건을 바꾸어 보세요.",
    "code": "scores = []\nfor i in range(5):\n    scores.append(int(input(f\"{i + 1} : 숫자를 입력하세요 : \")))\n\nprint(\"리스트변수의 값 : \", scores)\nfor number in scores:\n    if number % 2 == 0:\n        print(number)"
  },
  {
    "title": "구구단",
    "description": "중첩 반복문으로 2단부터 9단까지, 각 단의 1~9 곱셈을 출력합니다.",
    "challenge": "각 행과 열이 어떤 반복문에 해당하는지 Python 코드와 비교하세요.",
    "code": "for dan in range(2, 10):\n    for i in range(1, 10):\n        print(f\"{dan} x {i} = {dan * i}\", end=\"\\t\")\n    print()"
  },
  {
    "title": "숫자 맞추기",
    "description": "컴퓨터가 고른 1~100 사이의 정수를 맞혀 보세요. 입력할 때마다 힌트를 제공합니다.",
    "challenge": "범위를 반으로 좁히며 정답을 찾아보세요. 시도 횟수도 확인할 수 있습니다.",
    "code": "import random\n\ncom_number = random.randint(1, 100)\nuser_number = 0\n\nwhile com_number != user_number:\n    user_number = int(input(\"1~100 : \"))\n    if user_number > com_number:\n        print(\"컴퓨터보다 큽니다.\")\n    elif user_number < com_number:\n        print(\"컴퓨터보다 작습니다.\")\n    else:\n        print(\"정답입니다.\")"
  }
];


const $ = id => document.getElementById(id);
let selected = 0;
let answer = 0;
let attempts = 0;
let finished = false;
let history = [];

function field(id, label, value = "", placeholder = "정수 입력") {
  const wrapper = document.createElement("div");
  wrapper.className = "field";
  const labelNode = document.createElement("label");
  labelNode.htmlFor = id;
  labelNode.textContent = label;
  const input = document.createElement("input");
  input.id = id;
  input.type = "text";
  input.inputMode = "numeric";
  input.required = true;
  input.value = value;
  input.placeholder = placeholder;
  wrapper.append(labelNode, input);
  return wrapper;
}

function startGame() {
  answer = Math.floor(Math.random() * 100) + 1;
  attempts = 0;
  finished = false;
  history = [];
  $("run-button").disabled = false;
  $("guess").disabled = false;
  $("guess").value = "";
  $("error").textContent = "";
  $("result").replaceChildren();
  showLine("새 게임이 준비되었습니다. 1~100 사이의 숫자를 입력하세요.", "output-note");
}

function showLine(text, className = "result-line") {
  const p = document.createElement("p");
  p.className = className;
  p.textContent = text;
  $("result").append(p);
}

function chooseLesson(index) {
  selected = index;
  const lesson = lessons[index];
  $("lesson-number").textContent = `EXERCISE 0${index + 1} / 05`;
  $("lesson-title").textContent = lesson.title;
  $("lesson-description").textContent = lesson.description;
  $("source-code").textContent = lesson.code;
  $("challenge").textContent = lesson.challenge;
  $("fields").replaceChildren();
  $("result").replaceChildren();
  showLine("입력값을 설정하고 실행해 보세요.", "empty");
  $("error").textContent = "";
  $("run-button").disabled = false;
  $("reset-game").hidden = index !== 4;
  document.querySelectorAll("#lesson-nav button").forEach((button, i) => button.setAttribute("aria-pressed", String(i === index)));
  if (index === 0) {
    $("fields").append(field("number1", "첫 번째 숫자", "100"), field("number2", "두 번째 숫자", "200"));
  } else if (index === 1) {
    $("fields").append(field("score", "점수", "60"));
  } else if (index === 2) {
    const group = document.createElement("div");
    group.className = "number-fields";
    for (let i = 0; i < 5; i++) group.append(field(`list-${i}`, `숫자 ${i + 1}`, String(i + 1)));
    $("fields").append(group);
  } else if (index === 3) {
    const hint = document.createElement("p");
    hint.className = "hint";
    hint.textContent = "입력 없이 실행할 수 있습니다. 각 열은 2~9단, 각 행은 곱하는 숫자 1~9를 나타냅니다.";
    $("fields").append(hint);
  } else {
    $("fields").append(field("guess", "예상 숫자", "", "1~100"));
    startGame();
  }
}

lessons.forEach((lesson, index) => {
  const button = document.createElement("button");
  button.type = "button";
  const number = document.createElement("span");
  number.className = "num";
  number.textContent = `0${index + 1}`;
  const title = document.createElement("span");
  title.textContent = lesson.title;
  button.append(number, title);
  button.addEventListener("click", () => chooseLesson(index));
  $("lesson-nav").append(button);
});

$("practice-form").addEventListener("submit", event => {
  event.preventDefault();
  $("error").textContent = "";
  const integer = (id, label) => readInteger($(id).value, label);
  try {
    // 입력 검증이 성공한 뒤에만 이전 결과를 바꿉니다.
    if (selected === 0) {
      const a = integer("number1", "첫 번째 숫자");
      const b = integer("number2", "두 번째 숫자");
      const sum = addNumbers(a, b);
      $("result").replaceChildren();
      showLine(String(sum), "value");
      showLine(`${a} + ${b} = ${sum}`, "output-note");
    } else if (selected === 1) {
      const score = integer("score", "점수");
      $("result").replaceChildren();
      showLine(score >= 60 ? "합격" : "불합격", "value");
      showLine(`입력 점수: ${score} / 합격 기준: 60점 이상`, "output-note");
    } else if (selected === 2) {
      const values = Array.from({ length: 5 }, (_, i) => integer(`list-${i}`, `숫자 ${i + 1}`));
      const evens = evenNumbers(values);
      $("result").replaceChildren();
      showLine(`리스트: [${values.join(", ")}]`, "output-note");
      showLine(`짝수 ${evens.length}개`, "value");
      showLine(evens.length ? evens.join(", ") : "짝수가 없습니다.");
    } else if (selected === 3) {
      $("result").replaceChildren();
      const wrap = document.createElement("div");
      wrap.className = "table-wrap";
      const table = document.createElement("table");
      const caption = document.createElement("caption");
      caption.textContent = "2단부터 9단까지 구구단";
      table.append(caption);
      const head = table.createTHead().insertRow();
      for (let dan = 2; dan <= 9; dan++) {
        const th = document.createElement("th");
        th.scope = "col";
        th.textContent = `${dan}단`;
        head.append(th);
      }
      const body = table.createTBody();
      multiplicationRows().forEach(row => {
        const tr = body.insertRow();
        row.forEach(value => { tr.insertCell().textContent = value; });
      });
      wrap.append(table);
      $("result").append(wrap);
    } else {
      if (finished) return;
      const guess = integer("guess", "예상 숫자");
      if (guess < 1 || guess > 100) throw new Error("1~100 사이의 정수를 입력하세요.");
      attempts++;
      finished = guess === answer;
      history.push(`${attempts}회 · ${guess} → ${guessHint(guess, answer)}`);
      $("result").replaceChildren();
      showLine(finished ? "정답입니다!" : guessHint(guess, answer), "value");
      showLine(`시도 횟수: ${attempts}회`, "output-note");
      history.forEach(line => showLine(line));
      $("run-button").disabled = finished;
      $("guess").disabled = finished;
      if (!finished) { $("guess").select(); }
    }
  } catch (error) {
    $("error").textContent = error.message;
  }
});
$("reset-game").addEventListener("click", () => { startGame(); $("guess").focus(); });
chooseLesson(0);
