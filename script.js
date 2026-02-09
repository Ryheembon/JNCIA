(function () {
  'use strict';

  // Use the 100+ question bank
  const questions = typeof JNCIA_QUESTIONS !== 'undefined' ? JNCIA_QUESTIONS : [];
  const totalCount = questions.length;

  // Set hero stat
  const totalEl = document.getElementById('totalQuestions');
  if (totalEl) totalEl.textContent = totalCount;

  // --- Quiz state
  let quizQuestions = [];
  let quizIndex = 0;
  let quizScore = 0;
  let selectedOptionIndex = null;

  const quizSetup = document.getElementById('quizSetup');
  const quizArea = document.getElementById('quizArea');
  const quizResults = document.getElementById('quizResults');
  const quizQuestionText = document.getElementById('quizQuestionText');
  const quizOptions = document.getElementById('quizOptions');
  const quizFeedback = document.getElementById('quizFeedback');
  const feedbackResult = document.getElementById('feedbackResult');
  const feedbackExplanation = document.getElementById('feedbackExplanation');
  const nextQuestionBtn = document.getElementById('nextQuestionBtn');
  const progressFill = document.getElementById('progressFill');
  const quizProgressText = document.getElementById('quizProgressText');
  const runningScore = document.getElementById('runningScore');
  const runningTotal = document.getElementById('runningTotal');
  const finalCorrect = document.getElementById('finalCorrect');
  const finalTotal = document.getElementById('finalTotal');
  const finalPercent = document.getElementById('finalPercent');
  const startQuizBtn = document.getElementById('startQuizBtn');
  const categoryFilter = document.getElementById('categoryFilter');
  const questionCount = document.getElementById('questionCount');
  const retryQuizBtn = document.getElementById('retryQuizBtn');

  function getFilteredQuestions() {
    const category = categoryFilter ? categoryFilter.value : 'all';
    const max = Math.min(parseInt(questionCount ? questionCount.value : '20', 10) || 999, questions.length);
    let pool = category === 'all'
      ? questions.slice()
      : questions.filter(function (q) { return q.category === category; });
    // Shuffle
    for (let i = pool.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      const t = pool[i];
      pool[i] = pool[j];
      pool[j] = t;
    }
    return pool.slice(0, max);
  }

  function startQuiz() {
    quizQuestions = getFilteredQuestions();
    if (quizQuestions.length === 0) {
      alert('No questions match the selected topic. Try "All topics".');
      return;
    }
    quizIndex = 0;
    quizScore = 0;
    if (quizSetup) quizSetup.style.display = 'none';
    if (quizResults) quizResults.style.display = 'none';
    if (quizArea) quizArea.style.display = 'block';
    showQuestion();
  }

  function showQuestion() {
    const q = quizQuestions[quizIndex];
    if (!q) {
      showResults();
      return;
    }
    selectedOptionIndex = null;
    if (quizQuestionText) quizQuestionText.textContent = q.question;
    if (quizOptions) {
      quizOptions.innerHTML = '';
      q.options.forEach(function (opt, i) {
        const label = document.createElement('label');
        label.className = 'quiz-option';
        const radio = document.createElement('input');
        radio.type = 'radio';
        radio.name = 'quizOption';
        radio.value = i;
        radio.addEventListener('change', function () { selectedOptionIndex = i; });
        label.appendChild(radio);
        label.appendChild(document.createTextNode(' ' + opt));
        quizOptions.appendChild(label);
      });
    }
    if (quizFeedback) quizFeedback.style.display = 'none';
    updateProgress();
    if (runningScore) runningScore.textContent = quizScore;
    if (runningTotal) runningTotal.textContent = quizQuestions.length;
  }

  function updateProgress() {
    const total = quizQuestions.length;
    const pct = total ? (quizIndex / total) * 100 : 0;
    if (progressFill) progressFill.style.width = pct + '%';
    if (quizProgressText) quizProgressText.textContent = 'Question ' + (quizIndex + 1) + ' of ' + total;
  }

  function submitAnswer() {
    if (selectedOptionIndex === null) {
      alert('Please select an answer.');
      return;
    }
    const q = quizQuestions[quizIndex];
    const correct = selectedOptionIndex === q.correctIndex;
    if (correct) quizScore++;
    if (feedbackResult) {
      feedbackResult.textContent = correct ? 'Correct!' : 'Incorrect.';
      feedbackResult.className = 'feedback-result ' + (correct ? 'correct' : 'incorrect');
    }
    if (feedbackExplanation) {
      feedbackExplanation.textContent = 'Explanation: ' + (q.explanation || '');
    }
    if (quizFeedback) quizFeedback.style.display = 'block';
    if (runningScore) runningScore.textContent = quizScore;
  }

  function nextQuestion() {
    quizIndex++;
    if (quizIndex >= quizQuestions.length) {
      showResults();
      return;
    }
    showQuestion();
  }

  function showResults() {
    if (quizArea) quizArea.style.display = 'none';
    if (quizResults) quizResults.style.display = 'block';
    const total = quizQuestions.length;
    const pct = total ? Math.round((quizScore / total) * 100) : 0;
    if (finalCorrect) finalCorrect.textContent = quizScore;
    if (finalTotal) finalTotal.textContent = total;
    if (finalPercent) finalPercent.textContent = pct + '%';
  }

  function retryQuiz() {
    if (quizResults) quizResults.style.display = 'none';
    if (quizSetup) quizSetup.style.display = 'block';
  }

  if (startQuizBtn) startQuizBtn.addEventListener('click', startQuiz);
  if (nextQuestionBtn) {
    nextQuestionBtn.textContent = 'Submit answer';
    nextQuestionBtn.addEventListener('click', function () {
      if (quizFeedback && quizFeedback.style.display === 'block') {
        nextQuestion();
        nextQuestionBtn.textContent = 'Submit answer';
      } else {
        if (selectedOptionIndex === null) {
          alert('Please select an answer.');
          return;
        }
        submitAnswer();
        nextQuestionBtn.textContent = (quizIndex + 1 >= quizQuestions.length) ? 'See results' : 'Next question';
      }
    });
  }
  if (retryQuizBtn) retryQuizBtn.addEventListener('click', retryQuiz);

  // --- Flashcards (built from question bank)
  const flashcardList = questions.map(function (q) {
    return {
      category: q.category,
      question: q.question,
      answer: q.options[q.correctIndex] + '\n\n' + (q.explanation || '')
    };
  });
  let currentCards = flashcardList.slice();
  let currentCardIndex = 0;

  const flashcard = document.getElementById('flashcard');
  const flashcardQuestion = document.getElementById('flashcardQuestion');
  const flashcardAnswer = document.getElementById('flashcardAnswer');
  const prevCard = document.getElementById('prevCard');
  const nextCard = document.getElementById('nextCard');
  const cardCounter = document.getElementById('cardCounter');
  const flashcardCategory = document.getElementById('flashcardCategory');
  const flipCardBtn = document.getElementById('flipCardBtn');

  function filterFlashcards() {
    const cat = flashcardCategory ? flashcardCategory.value : 'all';
    currentCards = cat === 'all'
      ? flashcardList.slice()
      : flashcardList.filter(function (c) { return c.category === cat; });
    currentCardIndex = 0;
    updateFlashcard();
  }

  function updateFlashcard() {
    if (currentCards.length === 0) {
      if (flashcardQuestion) flashcardQuestion.textContent = 'No cards in this category.';
      if (flashcardAnswer) flashcardAnswer.textContent = '';
    } else {
      const card = currentCards[currentCardIndex];
      if (flashcardQuestion) flashcardQuestion.textContent = card.question;
      if (flashcardAnswer) flashcardAnswer.textContent = card.answer;
      if (flashcard) flashcard.classList.remove('flipped');
    }
    if (cardCounter) {
      cardCounter.textContent = currentCards.length
        ? (currentCardIndex + 1) + ' / ' + currentCards.length
        : '0 / 0';
    }
  }

  function prevFlashcard() {
    if (currentCards.length === 0) return;
    currentCardIndex = (currentCardIndex - 1 + currentCards.length) % currentCards.length;
    updateFlashcard();
  }

  function nextFlashcard() {
    if (currentCards.length === 0) return;
    currentCardIndex = (currentCardIndex + 1) % currentCards.length;
    updateFlashcard();
  }

  if (flashcardCategory) flashcardCategory.addEventListener('change', filterFlashcards);
  if (prevCard) prevCard.addEventListener('click', prevFlashcard);
  if (nextCard) nextCard.addEventListener('click', nextFlashcard);
  if (flipCardBtn) flipCardBtn.addEventListener('click', function () {
    if (flashcard) flashcard.classList.toggle('flipped');
  });
  if (flashcard) flashcard.addEventListener('click', function () {
    flashcard.classList.toggle('flipped');
  });
  filterFlashcards();

  // Smooth scroll for nav
  document.querySelectorAll('.main-nav a, .cta-button').forEach(function (a) {
    a.addEventListener('click', function (e) {
      const href = this.getAttribute('href');
      if (href && href.startsWith('#')) {
        e.preventDefault();
        const id = href.slice(1);
        const el = document.getElementById(id);
        if (el) el.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });
})();
