#!/usr/bin/env python3
"""Builds the unlisted cleanse program pages (spring-cleanse/, fall-cleanse/).

Edit the data below, then run:  python3 tools/build_cleanse.py
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIL = 'mailto:info@yogacybin.com?subject=Cleanse'
ASK = f'<a href="{MAIL}">ask Pasha</a>'


def L(url, text):
    return f'<a href="{url}" target="_blank" rel="noopener">{text}</a>'


def ul(items, cls=''):
    c = f' class="{cls}"' if cls else ''
    return f'<ul{c}>' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'


def ol(items):
    return '<ol>' + ''.join(f'<li>{i}</li>' for i in items) + '</ol>'


BF_OWN = 'Breakfast as you need it: skip it, or have a small, warm, well-cooked meal.'
BF_NONE = 'No breakfast.'
GREEN = '<a href="#green-drink">green drink</a>'
KITCHARI = '<a href="#kitchari">kitchari</a>'
SADHANA = 'Sadhana: your own yoga, pranayama and meditation.'

# ---------------------------------------------------------------- Spring (18 days)

SPRING_PHASE = {1: 'Prepare', 2: 'Prepare', 3: 'Prepare', 10: 'Deep cleanse', 11: 'Deep cleanse',
                12: 'Deep cleanse', 13: 'Break the fast'}
for _d in range(4, 10):
    SPRING_PHASE[_d] = 'Cleanse'
for _d in range(14, 19):
    SPRING_PHASE[_d] = 'Rebuild'

SPRING_TITLE = {1: 'Opening gathering', 2: 'Study and shop', 3: 'Study and shop', 4: 'The cleanse begins',
                5: 'Simplify', 6: 'Simplify further', 7: 'Kitchari for lunch', 8: 'One meal, if you choose',
                9: 'One meal, if you choose', 10: 'Deep cleanse begins', 11: 'Deep cleanse', 12: 'Deep cleanse',
                13: 'Break the fast', 14: 'Rasayana begins', 15: 'Widen the plate', 16: 'Two to three meals',
                17: 'More variety', 18: 'Closing celebration'}

SPRING_NOTE = {
    1: 'We meet to walk through the program together. Pasha will send the time and place.',
    2: 'Read through this page, then shop for food and supplies. Start any of the daily practices now to get your mindset strong.',
    3: 'Read through this page, then shop for food and supplies. Start any of the daily practices now to get your mindset strong.',
    4: 'The formal cleanse starts today. In your morning practice, light a candle for everyone on the cleanse.',
    10: 'Restorative yoga class today. Pasha will send the details.',
    12: 'It is fine to break your fast today if you are unwell.',
    18: 'Our final meeting is today. Share and celebrate!',
}

_DEEP = [BF_NONE, 'Same as Day 9, <em>or</em> water fast.',
         'If you feel lightheaded or weak, sip an electrolyte drink: warm water, honey, mineral salt, cayenne and apple juice.']
SPRING_FOOD = {
    4: ['Breakfast only if you are hungry: a small, warm, well-cooked meal. Otherwise tea, golden milk or a ' + GREEN + '.',
        'Cut out processed foods, sugar, coffee, alcohol, recreational drugs, soda and any food you know you are allergic to.',
        'No sweeteners except local honey. Apple juice is fine.'],
    5: [BF_OWN, 'Also cut out gluten, eggs and dairy (ghee is fine).',
        'Eat 2–3 simple, clean meals: bean and vegetable soups, steamed vegetables with ghee and salt, cooked grains, salad greens, beans (sprouted are best).',
        'Eat fruit on its own. Apples are great.'],
    6: [BF_OWN, 'Same as Day 5. Also cut out all wheat, anything with additives or preservatives, nightshades (peppers, tomatoes, white potatoes), spinach and caffeine.',
        'Drink plenty of warm water with lemon or lime. Apple juice is fine.'],
    7: [BF_OWN, 'Same as Day 6, with ' + KITCHARI + ' for lunch. Top it with plenty of ghee and fresh cilantro.',
        'Drink hot water or herbal and cleansing teas.', 'No food after 6 pm.'],
    8: [BF_OWN, 'Same as Day 7, <em>or</em> eat one meal only: kitchari with vegetables in the middle of the day, skipping breakfast and dinner.',
        'Drink hot water with lemon or lime, or herbal and cleansing teas.'],
    9: [BF_NONE, 'Same as Day 7, <em>or</em> eat one meal only: kitchari with vegetables in the middle of the day.',
        'Drink hot water with lemon or lime, or herbal and cleansing teas.'],
    10: _DEEP, 11: _DEEP, 12: _DEEP,
    13: ['Break your fast at late breakfast or midday with kanji (watery rice with ghee and salt; peas are fine) or kitchari.',
         'Add a ' + GREEN + ' and chew it. You can have it at dinner instead.'],
    14: [BF_OWN, 'Back to 2 meals: kitchari with greens, sprouts or asparagus. A different soup is fine too.',
         'Add a <a href="#probiotics">probiotic food</a> with your meal: mild kimchi, horseradish or kombucha. Wait one more day for dairy.'],
    15: [BF_OWN, 'Same as Day 14, with more variety: millet, quinoa or buckwheat, and more vegetables (still no nightshades).',
         'Some salad with a little oil or avocado.',
         'Probiotic food with a meal. Kefir, yogurt or a <a href="#lassi">savory lassi</a> are fine from today.'],
    16: [BF_OWN, 'Eat 2–3 meals. One can be a fruit salad, but not lunch. It does not have to be kitchari, but hold off on strong, pungent spices.',
         'Other dairy, healthy sweeteners and healthy fats are fine if you want them.', 'Probiotic food with a meal.'],
    17: [BF_OWN, 'Same as Day 16. You can add more pungent spices and a wider range of grains, beans, vegetables, nuts and fruits.',
         'Still no snacking between meals.', 'Probiotic food with a meal.'],
    18: [BF_OWN, '2–3 clean meals, still no snacking. Add eggs if you like.', 'Probiotic food with a meal.'],
}

SPRING_OLE = {4: '1–2 tablespoons', 5: '2–3 tablespoons', 6: '3–4 tablespoons', 7: '4–5 tablespoons'}


def spring_morning(d):
    o = []
    if d in SPRING_OLE:
        o.append(f'Optional <a href="#oleation">oleation</a>: {SPRING_OLE[d]} of melted ghee, after your warm water and before sadhana.')
        o.append('If you oleate, do <a href="#agni-sara">Agni Sara</a> during sadhana.')
    if d == 8:
        o.append('No more oleation for the rest of the cleanse.')
    if d == 10:
        o.append('Sadhana: restorative yoga class.')
    elif d in (11, 12):
        o.append('Sadhana: less asana, more meditation, pranayama, yoga nidra or legs up the wall.')
    elif d == 18:
        o.append('Sadhana: your own practice, then final sharing with everyone.')
    elif d >= 4:
        o.append(SADHANA)
    return o


def spring_body(d):
    o = []
    if d == 4:
        o.append('Start daily <a href="#abhyanga">abhyanga</a> (self-massage with oil), before or after your bath or shower.')
    elif d > 4:
        o.append('Light <a href="#abhyanga">abhyanga</a>.')
    if d in (10, 11, 12):
        o.append('Optional heavier abhyanga with castor oil before sweating.')
    if 10 <= d <= 13:
        o.append('<a href="#garshana">Garshana</a> (dry brushing) before your bath or shower.')
        o.append('<a href="#swedana">Swedana</a> (sweating): sauna or hot bath, 20 minutes at most. Drink plenty of water afterwards.')
    return o


def spring_evening(d):
    o = []
    if 7 <= d <= 10:
        o.append('<a href="#triphala">Triphala</a> tea 1 hour before bed: 1 tsp powder in 1 cup of water, or 2 tablets.'
                 + (' Reduce the dose if you get diarrhea or cramping.' if d > 7 else ''))
    if 12 <= d <= 16:
        o.append('Optional <a href="#basti">basti</a> this evening. Do it on any two nights between Day 12 and Day 16, twice in total, and take a probiotic food afterwards.')
    if d >= 14:
        o.append('<a href="#rasayana">Rasayana</a> 1 hour before bed.' + (' Keep taking it for another week.' if d == 18 else ''))
    return o


def spring_days():
    days = []
    for d in range(1, 19):
        days.append(dict(
            num=d, phase=SPRING_PHASE[d], title=SPRING_TITLE[d], note=SPRING_NOTE.get(d),
            jump=(d in (2, 3)), routine=(d >= 4),
            sections=[('Food', SPRING_FOOD.get(d, [])), ('Morning', spring_morning(d)),
                      ('Body care', spring_body(d)), ('Evening', spring_evening(d))]))
    return days


# ---------------------------------------------------------------- Fall (15 days)

FALL_PHASE = {}
for _d in range(1, 7):
    FALL_PHASE[_d] = 'Ease in'
for _d in (7, 8, 9):
    FALL_PHASE[_d] = 'Deep cleanse'
FALL_PHASE[10] = 'Break the fast'
for _d in range(11, 16):
    FALL_PHASE[_d] = 'Rebuild'

FALL_TITLE = {1: 'The cleanse begins', 2: 'Let go of more', 3: 'Lighter still', 4: 'Simple and clean',
              5: 'Restorative evening', 6: 'One meal', 7: 'Deep cleanse begins', 8: 'Fast', 9: 'Fast',
              10: 'Break the fast', 11: 'Build back', 12: 'Rasayana begins', 13: 'Rest and rebuild',
              14: 'Almost there', 15: 'You made it'}

FALL_NOTE = {
    1: 'The cleanse officially starts today.',
    5: 'Optional restorative yoga class this evening. Pasha will send the details. Afterwards go home and straight to bed.',
    8: 'Do not spend the day working or socializing. Sadhana, ceremony, journaling, write a letter, walk or sit somewhere beautiful, practise silence, listen deeply inside and out.',
    9: 'Do not spend the day working or socializing. Sadhana, ceremony, journaling, write a letter, walk or sit somewhere beautiful, practise silence, listen deeply inside and out.',
    15: 'You made it! We gather and share today. Keep your diet and lifestyle this clean for as long as you can.',
}

LIVER = 'Liver support: a glass of celery juice or a shot of cilantro juice, 30 minutes after a cup or two of lemon water.'
_FAST = ['Fast: lemon water, ginger and turmeric tea, herbal teas. A juice fast is fine if you prefer.']
FALL_FOOD = {
    1: ['Cut out junk food, recreational drugs and alcohol.',
        'After practice, more lemon water (any temperature), then celery juice and/or a light breakfast.',
        'A generally healthy diet today.'],
    2: ['Also cut out sugar, coffee, meat, and foods with additives or preservatives.',
        'A healthy vegetarian diet. Keep up the lemon water and herbal teas.'],
    3: ['Also cut out eggs, dairy, wheat and fried foods.',
        'More soups, salads and sprouts. Steamed greens with tamari and sesame oil, or roasted fall vegetables, are excellent.',
        'Skip dinner, or have only miso soup with greens, tofu and scallions.'],
    4: ['A simple, clean diet with lots of vegetables, like yesterday. Drink lots of purified water.',
        'If you relied on coffee to move your bowels, have prunes stewed in water with a little cinnamon; they make a delicious breakfast.',
        'Dinner very light (broth or fruit), or skip it.'],
    5: ['Start the day with 16 oz of lemon water. Skip breakfast if you can, or keep it light; 16 oz of celery juice is excellent, 30 minutes after the water.',
        'Lunch: vegetable soup with rice, quinoa, millet or barley (not wheat), or ' + KITCHARI + '.'],
    6: ['One meal, at midday: ' + KITCHARI + '.', 'Teas and water through the day.'],
    7: ['Water fast, juice fast, or one meal at midday: kitchari.',
        'Teas and water through the day. Cucumber or celery juice are excellent (cucumber is very hydrating but can make you cold).'],
    8: _FAST, 9: _FAST,
    10: ['Lemon water first thing; 30 minutes later, celery or cilantro juice.',
         'Break your fast at midday with watery rice gruel with a little miso and some greens stirred in.',
         'In the evening, if your body feels hungry and ready, some cooked vegetables with a little grain (not wheat). Eat before 6:30.',
         'Keep drinking teas.'],
    11: ['Like yesterday, with a little more quantity. A light breakfast is fine.',
         'You are building back up: add some fruit, a little oil or butter, even dairy, but keep it very clean. Roasted root vegetables are still excellent. Cooked beans are fine today.',
         'Start a <a href="#probiotics">probiotic</a>.'],
    12: ['Same as yesterday.', 'Probiotic.'],
    13: ['Same as yesterday. Keep dinner light.', 'Still no meat, alcohol, junk food or sugar.', 'Probiotic.'],
    14: ['Same as yesterday. Add eggs and other grains if you wish.', 'Probiotic.'],
    15: ['Same as yesterday.', 'Probiotic.'],
}

FALL_OLE = {1: '1 tablespoon', 2: '2 tablespoons', 3: '3 tablespoons'}


def fall_morning(d):
    o = []
    if d in FALL_OLE:
        o.append(f'Optional <a href="#oleation">oleation</a>: a few sips of hot water, then hot lemon water, and 5 minutes later {FALL_OLE[d]} of melted ghee, coconut or flax oil. Sip the rest of the cup.')
        o.append('If you oleate, do <a href="#agni-sara">Agni Sara</a> about 20 minutes later, during sadhana.')
    if d == 4:
        o.append('No more oleation for the rest of the cleanse.')
    if d <= 11:
        o.append(LIVER)
    if d in (8, 9):
        o.append('Sadhana: more meditation, pranayama and stillness than asana.')
    elif d == 15:
        o.append('Sadhana: your own practice, then gather and share.')
    else:
        o.append(SADHANA)
    return o


def fall_body(d):
    o = []
    if d == 1:
        o.append('Start daily <a href="#abhyanga">abhyanga</a> (self-massage with oil), before or after your bath or shower.')
    else:
        o.append('Light <a href="#abhyanga">abhyanga</a>.')
    if 6 <= d <= 10:
        o.append('<a href="#garshana">Garshana</a> (dry brushing) before your bath or shower, followed if you like by abhyanga with a little castor oil.')
        o.append('<a href="#swedana">Swedana</a> (sweating): sauna or hot bath, 20 minutes at most. Drink plenty of water afterwards.')
    return o


def fall_evening(d):
    o = []
    if d in (3, 4, 5, 6):
        o.append('Light or no dinner (see Food), and an early night.')
    if d == 9:
        o.append('Optional <a href="#basti">basti</a> at the end of today.')
    if d == 10:
        o.append('Optional <a href="#basti">basti</a> tonight, again or for the first time.')
    if d == 11:
        o.append('Optional <a href="#basti">basti</a> before bed, for the first, second or final time. Take a probiotic afterwards.')
    if d >= 12:
        o.append('<a href="#rasayana">Rasayana</a> 1–2 hours before bed: an ojas-building shake, golden milk or chyavanprash.'
                 + (' Keep taking it for another two weeks.' if d == 15 else ''))
    return o


def fall_days():
    days = []
    for d in range(1, 16):
        days.append(dict(
            num=d, phase=FALL_PHASE[d], title=FALL_TITLE[d], note=FALL_NOTE.get(d), jump=False, routine=True,
            sections=[('Food', FALL_FOOD.get(d, [])), ('Morning', fall_morning(d)),
                      ('Body care', fall_body(d)), ('Evening', fall_evening(d))]))
    return days


FALL_BEFORE = '''
    <section class="before" id="before">
      <p class="phase">Before Day 1</p>
      <h2>Gather and prepare</h2>
      <ul>
        <li><b>Gathering:</b> we meet to walk through the program together. Pasha will send the time and place.</li>
        <li><b>The three days before:</b> shop for supplies (see the <a href="#shopping">shopping list</a>), read this page, and prepare mentally. If you like, start cutting out the things that do not support you now.</li>
      </ul>
    </section>
'''

# ---------------------------------------------------------------- Shared reference content


def guides(season):
    spring = season == 'spring'
    ole_sched = ('Days 4 to 7 of the spring cleanse: 1–2, 2–3, 3–4, then 4–5 tablespoons.' if spring
                 else 'Days 1 to 3 of the fall cleanse: 1, 2, then 3 tablespoons.')
    basti_when = ('Do it in the evening on any two nights between Day 12 and Day 16, twice in total.' if spring
                  else 'Do it in the evening on Day 9, 10 or 11, up to three times in total.')
    ras_when = 'From Day 14, and for a week after the cleanse ends.' if spring else 'From Day 12, and for two weeks after the cleanse ends.'
    g = []

    def add(id, title, tag, body):
        g.append(f'<details id="{id}"><summary>{title} <span class="tag">{tag}</span></summary><div>{body}</div></details>')

    add('oleation', 'Oleation', 'Optional · ' + ('Days 4–7' if spring else 'Days 1–3'),
        '<p>Oleation, or <em>snehakarma</em>, loosens ama (toxicity) and imbalanced doshas from the inner tissues so they can be released. For the cleanse we use ghee, tikta ghee, sesame oil, coconut oil (if you are vegan) or flax oil. Never heat flax oil.</p>'
        '<p>Take it in the morning after cleaning your mouth, about 10 minutes after your hot water and before sadhana. The amount rises each day:</p>'
        f'<p><b>{ole_sched}</b></p>'
        '<p>Some resistance to drinking that much oil is normal. If you feel nauseous, add a pinch of black pepper or dry ginger to the oil. If the nausea is strong, or you get diarrhea, take less. Sip hot water or hot lemon water afterwards, then begin your sadhana.</p>'
        '<p>You will know you are sufficiently oiled when your stools look fluffy, ashen-grey, and break apart when they hit the water. If you have not reached that by the last oleation day, keep adding ghee to your kitchari and other food.</p>'
        '<p>Tikta ghee is a very bitter ghee that is especially good for expelling excess Pitta and Kapha; find it ' + L('https://vadikherbs.com/products/tikta-ghrita-bitter-ghee-7oz', 'online') + '. For more detox power, or to clear your skin, you can take 2 ' + L('https://www.banyanbotanicals.com/neem-tablets-10/', 'neem tablets') + ' with your oleation or throughout the cleanse.</p>'
        '<p class="warn">Skip oleation entirely if you do not have a gallbladder, if you have gallbladder or liver problems, or if the nausea is extreme.</p>')

    add('agni-sara', 'Agni Sara', 'With oleation',
        '<p>A kriya that massages the abdominal organs. Do 3 repetitions during sadhana, on an empty stomach, about 10–20 minutes after oleation. Superb during a cleanse.</p>'
        '<p>' + L('https://www.youtube.com/watch?v=vhM0fjR_yr8', 'Watch the Agni Sara technique') + '</p>')

    add('sadhana', 'Sadhana: yoga, pranayama, meditation', 'Every day',
        '<p>Your spiritual practice, every day of the cleanse. Choose your own yoga, breathwork and meditation, prayer or chanting. If Ayurvedic yoga is new to you, read ' + L('https://www.banyanbotanicals.com/info/ayurvedic-living/living-ayurveda/yoga/', 'this introduction') + f' or {ASK} for guidance.</p>')

    add('oil-pulling', 'Oil pulling', 'Optional · Every morning',
        '<p>A time-tested Ayurvedic practice that draws microbes out through the soft tissues of the mouth. It supports the gums and teeth, and its effects build up over 4–6 weeks of daily practice.</p>'
        + ol(['In the morning, take a little less than 1 tablespoon of organic, cold-pressed oil into your mouth. Coconut, sesame or sunflower oil are all good; avoid cheap commercial corn, soy or “vegetable” oils.',
              'Swish with some vigour for 5–10 minutes: pull it between the teeth and around the cheeks and gums. Make the bed, feed the cat or stretch while you swish. The oil turns thin, foamy and whitish.',
              '<b>Do not swallow.</b> Spit it out and rinse your mouth with warm water. Then scrape your tongue, and brush and floss as usual.',
              'Run hot water down the drain for a minute afterwards so the oil does not clog the pipes.'])
        + '<p>You can repeat it at night if you wish.</p>')

    add('tongue', 'Tongue scraping', 'Optional · Morning and evening',
        '<p>Look at your tongue in the morning before oil pulling or brushing. A whitish, foul-smelling coating is ama from incomplete digestion, often simply from eating late the night before. A yellowish tone points to raised Pitta, greyish to raised Vata; scalloped edges from the teeth show incomplete digestion in the small intestine.</p>'
        '<p>That coating is full of bacteria and the main cause of bad breath. Scraping it off daily cleans the mouth, gently stimulates the organs reflected on the tongue, and lets you taste your food properly, so you crave less sweet and salt.</p>'
        + ol(['After brushing and oil pulling, stand over the sink. Press the edge of the scraper moderately into the back of the tongue and pull it to the tip in one long, smooth stroke.',
              'Repeat 3–6 times, moving slightly to each side so you cover the whole surface. Do not scrape so hard that you hurt the taste buds.',
              'A slight gag reflex at first is normal, and it can help bring up mucus from the back of the throat.',
              'Rinse the scraper with hot water and let it air dry. Clean it with alcohol or hydrogen peroxide now and then. Stainless steel is the most hygienic.'])
        + '<p>No scraper? A spoon with a slightly sharp edge will do, though not as well. A toothbrush is not effective on the tongue.</p>')

    add('abhyanga', 'Abhyanga (oil massage)', 'Recommended · Every day',
        '<p>Self-massage with warm oil: anoint your sacred temple. Strongly recommended for everyone, especially with high Vata. Use sesame, almond or jojoba oil, or a dosha-specific oil. Do it in the morning or evening, classically before your bath or shower, or afterwards if you would rather keep oil out of the tub.</p>'
        '<p>On the sweating days you can go deeper with castor oil before swedana, as described in ' + L('http://ayurveda.alandiashram.org/ayurvedic-healing/spring-self-care?rq=bath', 'this self-care guide') + '.</p>')

    add('garshana', 'Garshana (dry brushing)', 'Days 10–13' if spring else 'Days 6–10',
        '<p>Dry brushing exfoliates, moves lymph, reduces ama and improves circulation. Before your bath or shower, brush the dry skin to bring blood to the surface. You do not need silk gloves or a special brush: exfoliating gloves or a rough old towel work. A must if you have a lot of Kapha imbalance or ama; in that case follow it with abhyanga using a little castor oil.</p>'
        '<p>' + L('https://www.youtube.com/watch?v=B8x7PU-T3ws', 'Watch the garshana technique') + '</p>')

    add('swedana', 'Swedana (sweating)', 'Days 10–13' if spring else 'Days 6–10',
        '<p>Purging through the skin. If you fast, sweat each day of the deep cleanse plus a day on either side. Use a sauna or simply a hot bath, for no more than 20 minutes, and drink plenty of water afterwards. If you run very Pitta, wrap your head in a cold towel.</p>'
        '<p>For more heat and drawing power, add to the bath ¼ cup ginger powder, ¼ cup baking soda and 1 cup Epsom salt. Skip the ginger if you are very Pitta.</p>')

    add('triphala', 'Triphala', 'Days 7–10' if spring else 'Optional',
        ('<p>Taken as a tea 1 hour before bed on Days 7 to 10: 1 teaspoon of powder in 1 cup of water, or 2 tablets. Reduce the dose if you get diarrhea or cramping.</p>' if spring else
         '<p>A gentle herbal purgative, superb for Ayurvedic cleanses. If you use it, take it as a tea 1 hour before bed in the days before any basti: 1 teaspoon of powder in 1 cup of water, or 2 tablets. Reduce the dose if you get diarrhea or cramping.</p>')
        + '<p>Available at Natural Grocers or from ' + L('https://www.banyanbotanicals.com/catalogsearch/result/?q=triphala', 'Banyan Botanicals') + '.</p>')

    add('basti', 'Basti', 'Optional · ' + ('Days 12–16' if spring else 'Days 9–11'),
        '<p>A warm, oily, medicated enema, superb for releasing excess Vata from the lower body, especially aches in the legs, hips and low back. It is done after purgation (triphala). You can skip the medicated part (dashamula, or ten-roots tea) and use just warm water and sesame oil.</p>'
        f'<p><b>{basti_when}</b> Take a probiotic food afterwards. Read the whole procedure before you begin, and the ' + L('https://www.ayurveda.com/resources/cleansing/basti', 'general information and contraindications') + '.</p>'
        '<h4>Prepare</h4>'
        + ol(['Eat kitchari for lunch. About an hour before sunset, instead of dinner, prepare the basti.',
              '<b>Dashamula tea:</b> boil 3 cups of pure water, add 2 tablespoons of dried dashamula, turn off the heat and steep for 10 minutes. Strain very well through a silk cloth or coffee filter; only the liquid goes in the bag.',
              'Blend the tea with ½ cup of sesame oil (not toasted) until emulsified. It must be body temperature or slightly warmer, <b>not hot</b>.',
              'Warm up the bathroom. Lay old towels on the floor to lie on (there may be some leakage), with a small pillow for your head, and keep a towel handy as a “diaper” for getting to the toilet.',
              'Find a place above you to hang the bag, such as a towel bar, where you can still reach the clip on the hose while lying down.',
              'Pour the mixture into the clean, air-dried bag. Run a little through the hose over the sink to check the flow and let the air out.',
              'Lubricate the nozzle, and yourself, with sesame oil. Do not use petroleum-based jelly even if the kit says so.'])
        + '<h4>Administer</h4>'
        + ol(['Lie on your left side. Gently and slowly insert the nozzle; if it is uncomfortable, try another angle. Release the clip bit by bit and let the liquid flow in.',
              'When the bag is empty, slowly remove the nozzle. Holding the liquid in, stay on your left side for 10 minutes.',
              'Roll onto your back for 10 minutes. Lift into a slight bridge pose for about 5 breaths, then lower and massage your belly 3–5 times: up the lower left, across just under the ribs, and down the lower right to the inner hip. This follows the colon in reverse.',
              'Roll onto your right side and rest for 10 minutes.',
              'Retain the enema for the full 30 minutes, and longer if you can, even until morning. But <b>never hold it longer than the body’s natural urge to eliminate</b>, even if that means getting up at 2 am. A pad or some folded tissue in your underwear guards against leakage.',
              'After using the toilet, keep resting or go back to bed. Do not be surprised if much less comes out than went in; trust your body to absorb what it needs. Bathe or shower as needed.'])
        + '<p>The next day most people feel mentally clear, grounded and more connected to the lower body, and aches in the low back, hips and legs often ease. If not, try another basti on one of the remaining nights.</p>'
        '<p><b>Equipment:</b> an enema bag with a hook is the simplest; a bucket kit is easier to keep clean but needs a secure way to hang it. Disposable kits are not recommended. Dashamula and sesame oil are sold by Banyan Botanicals.</p>')

    add('rasayana', 'Rasayana', 'Days 14–18' if spring else 'Days 12–15',
        '<p>Rasayanas, or rejuvenatives, rebuild <em>ojas</em>, the refined essence of good digestion that Ayurveda regards as the root of immunity and vitality. The body normally needs 30–35 days to make a little of it from food; certain foods and herbs nourish it directly: fresh whole milk, dates, almonds, saffron, cardamom, ashwagandha, shatavari and chyavanprash.</p>'
        f'<p><b>{ras_when}</b> Take it warm in the evening, an hour or two before bed, or in place of dinner. Choose one:</p>'
        '<h4 id="ojas-shake">Ojas-building shake</h4>'
        + ol(['Pour hot water over 10–12 almonds and soak them for several hours or overnight. Squeeze off the skins (optional, but easier to digest, especially for Vata).',
              'Blend the almonds with 1–2 pitted dates, 1 cup of milk or almond milk and a pinch of cardamom until slightly foamy.',
              'Optional: a pinch of dry ginger if digestion is sluggish, a very small pinch of saffron, or a pinch of ashwagandha or shatavari. Add turmeric and ginger to make it more like golden milk. Double it for two.'])
        + '<h4>Chyavanprash</h4><p>A sweet, spicy herbal jam (it contains cane sugar), from ' + L('http://www.banyanbotanicals.com/chyavanprash-7/', 'Banyan Botanicals') + '. Blend a heaped teaspoon into warm milk until frothy.</p>'
        '<h4>Golden milk</h4><p>Warm milk with turmeric, ginger and a pinch of black pepper is a perfectly good rasayana on its own.</p>')

    add('probiotics', 'Probiotics and savory lassi', 'Rebuild days',
        '<p>After the fast, a probiotic food with your meal helps rebuild the gut: mild kimchi, horseradish, kombucha, or miso with live cultures. Once dairy is back, kefir, yogurt or a savory lassi are excellent.</p>'
        '<h4 id="lassi">Savory lassi</h4>'
        '<p>Not the sweet mango lassi of restaurant menus, which mixes fruit and dairy, a poor combination in Ayurveda. The savory version is the one to drink during a cleanse, a little before and during a meal.</p>'
        + ol(['Mix plain, cultured, full-fat yogurt with water, 1:1.',
              'Add a pinch each of salt, black pepper, cumin powder and coriander powder.',
              'In hot weather, blend in a chunk of cucumber. If dairy makes you a little congested, add a pinch of dry ginger.'])
        + '<p>Drink half or all of it before the meal and it works as an excellent probiotic; the rest can go with the meal. It tastes a bit like a creamy salad dressing.</p>')

    add('neti', 'Neti pot and nasya', 'Optional · Any day',
        '<p><b>Neti</b> rinses the nasal passages with warm salt water. It clears mucus and irritants such as pollen, dust and pollution, reduces congestion and sinus pain, and helps with colds and seasonal allergies.</p>'
        + ol(['Add about ½ teaspoon of natural, non-iodized salt to warm distilled or previously boiled water in the pot, and swirl until it dissolves. If your problem is dryness rather than congestion, add a little ghee or oil.',
              'Lean over the sink and put the spout in the right nostril. Turn your head so the left ear is over the sink.',
              'Pour gently until the water trickles out of the left nostril.',
              'Face the sink and blow gently through both nostrils, pinching the nose to squeeze out the moisture, or blow into a tissue. Do not drop your head back; if water gets into the upper sinuses, just blow it out.',
              'Switch sides.'])
        + '<p>To open the sinuses more, in the bath or shower slowly push your little finger up the nostril and hold until it releases.</p>'
        '<p><b>Nasya:</b> a few drops of coconut or sesame oil, or a herbal nasya oil, in each nostril. Can be done daily.</p>')

    add('herbs', 'Other herbal support', 'Optional',
        '<p>Herbs add benefit, but also cost and complexity. Milk thistle is welcome throughout, and malic acid' + ('' if spring else ', celery juice or cilantro juice') + ' for liver support' + (' through Day 9' if spring else ' through Day 11') + '. Medicinal mushrooms, nettles, oatstraw, horsetail, mint, cloves, anise and chamomile are all good.</p>'
        f'<p>Manjistha, ashwagandha, shatavari, tulsi and brahmi are excellent too; {ASK} for specifics on these.</p>')

    add('inner', 'Emotional work', 'Optional',
        '<p>Write a letter, have a conversation, forgive someone, make amends, set a boundary, let go. Even if you do not choose this, emotions are likely to surface during the cleanse. Take good care of them: acknowledge them, thank them and let them flow through you.</p>')

    add('nature', 'Nature and sound', 'Optional',
        '<p>Lean against a tree, lie on the earth, soak up the sun, walk barefoot, do a slow walking meditation, gaze at the moon, work the soil.</p>'
        '<p>Sing, hum or practise Bhramari breath: a strong vibration in the upper body tones the vagus nerve.</p>')

    add('more', 'More ideas', 'Optional',
        '<p>Clean a closet, wash out the fridge, pray before meals, create a bedtime ritual, journal, play an instrument, chant, practise japa, bathe with Epsom salts, make art, dance, plant seeds. What else?</p>'
        '<p>Further reading: ' + L('http://ayurveda.alandiashram.org/ayurvedic-healing/digestive-enzymes', 'a word about digestive enzymes') + '.</p>')
    return '\n      '.join(g)


def routine(start_day):
    return f'''
    <section class="block" id="routine">
      <h2>Daily routine</h2>
      <p>Every day of the cleanse{', from Day ' + str(start_day) if start_day > 1 else ''}. The order of the morning steps can vary.</p>
      <h3>Morning</h3>
      <ol class="routine">
        <li><b>Wake early</b>, ideally at sunrise.</li>
        <li><b>First thought:</b> a prayer, mantra or visualization for one minute, such as “24 brand new hours”.</li>
        <li><b>Eliminate</b>, and observe. Urine is ideally clear and medium yellow. Notice undigested food or an unusually strong smell.</li>
        <li class="opt"><b>Oil pulling</b>, brush teeth, <b>scrape tongue</b>. <a href="#oil-pulling">How</a></li>
        <li><b>Warm water:</b> one cup or less, purified, never cold. Lemon or lime if you like; lime is better for high Pitta.</li>
        <li class="opt"><b>Oleation</b> on the oleation days. <a href="#oleation">How</a></li>
        <li><b>Sadhana:</b> yoga, pranayama, then meditation, prayer or chanting. <a href="#sadhana">More</a></li>
        <li class="opt"><b>Bath or shower with abhyanga.</b> <a href="#abhyanga">How</a></li>
      </ol>
      <h3>Through the day</h3>
      <ul class="routine">
        <li><b>Rest. This one is not optional.</b> Your body, mind and spirit are going through a gentle but deep transformation. Do not schedule a lot of work or socializing, especially during the deep cleanse. Nap and put your legs up the wall when you need to.</li>
        <li class="opt"><b>Neti, nasya, time in nature, singing, emotional work.</b> <a href="#guide">See the practice guide</a></li>
      </ul>
      <h3>Evening</h3>
      <ul class="routine">
        <li><b>Screens off by 9 pm</b> or earlier. Dim the lights or use candles.</li>
        <li><b>Wind down:</b> read, gentle yoga, meditation, trataka, journaling, legs up the wall, yoga nidra, prayer, counting blessings, time with family.</li>
        <li><b>In bed by 10.</b> Lengthen your exhalations as you lie down.</li>
        <li>Reduce or pause sexual activity, and fast from violent or disturbing films, news and images, and from too much screen time.</li>
      </ul>
      <p class="key"><span class="dot"></span> Core practice <span class="dot opt"></span> Optional</p>
    </section>
'''


def food(season):
    spring = season == 'spring'
    seasonal = ('Favor root vegetables, peas, asparagus, greens and sprouts.' if spring
                else 'Favor root vegetables, winter squash, greens and sprouts.')
    kitchari_season = ('For spring, cook in sprouts, beets, asparagus, dandelion or other bitter greens, which support the liver and get bile moving.' if spring
                       else 'For fall, cook in cubed sweet potato, squash or other root vegetables.')
    return f'''
    <section class="block" id="food">
      <h2>Food basics</h2>
      <ul>
        <li>Home-cooked, fresh, seasonal, organic, local, real food.</li>
        <li>Mineral-rich salt; no refined oils.</li>
        <li>No snacking between meals.</li>
        <li>Sip warm or hot water, CCF tea (cumin, coriander, fennel) or herbal teas through the day. Tulsi, brahmi, ginger, mint and detox blends are all great.</li>
        <li>Avoid nightshades. {seasonal}</li>
        <li>Try eating in silence, as a meditation.</li>
      </ul>
      <h3>Breakfast</h3>
      <p>Skip it if you are not hungry. Otherwise keep it small, warm and well cooked: oatmeal, cooked buckwheat, or eggs while they are still allowed. For sweetness use dates, prunes or honey; prunes stewed in water with cinnamon are excellent. Avoid salsa, sugar, cold cereal, frozen foods and smoothies that mix fruit and vegetables.</p>
      <h3 id="kitchari">Kitchari</h3>
      <p>The perfect cleanse food: a thick, warming soup of white basmati rice and split yellow mung beans, both so easy to digest that in India they are fed to babies and elders. Make a pot or two and eat it often. {kitchari_season} Serve with fresh cilantro, a little more ghee and a squeeze of lime.</p>
      <details id="kitchari-recipe"><summary>Kitchari recipe <span class="tag">About 4 servings</span></summary><div>
        {ol(['Rinse 1 cup white basmati rice (or quinoa) and 1 cup split yellow mung beans (mung dal). Cook them together in 4–6 cups of water until they begin to soften. Add cubed vegetables now; add greens later, as they cook quickly.',
             'In a small pot, melt 2 tablespoons of ghee and fry, in this order: 1–2 teaspoons diced fresh ginger, 1 teaspoon black or brown mustard seeds, 1–2 teaspoons cumin seeds, 1 teaspoon fennel seeds.',
             'Turn off the heat and stir in 2 teaspoons coriander powder, 2 teaspoons turmeric, a small pinch of hing (asafoetida; skip if you have none) and a little freshly ground black pepper.',
             'Add the spices to the pot and keep cooking on medium-low, adding water as needed, until the grains are almost indistinguishable. The right consistency is like slightly thin oatmeal.',
             'Salt to taste at the end. Add more of any of the spices, or dry ginger, if you like it spicier.'])}
        <p>If you would rather watch: {L('http://www.youtube.com/watch?v=JLJN6ENjGbc', 'a kitchari video')}, and {L('https://www.banyanbotanicals.com/info/ayurvedic-living/living-ayurveda/diet/how-to-make-kitchari/', 'Banyan’s extensive guide')}.</p>
      </div></details>
      <h3 id="green-drink">Green drink</h3>
      <p>Cucumber, celery, apple, ginger, lemon or lime, and cilantro or parsley. Nothing frozen. “Chew” it rather than gulping it down.</p>
    </section>
'''


def shopping(season):
    spring = season == 'spring'
    veg = ('Fresh vegetables you love and will eat. Sprouts, beets, asparagus and bitter greens are great in spring.' if spring
           else 'Fresh vegetables you love and will eat. Root vegetables, greens and squashes are great in fall.')
    fruit = ('Fresh fruit in season; apples are great.' if spring else 'Fresh fruit in season: apples, pears, plums and some citrus.')
    core = [
        'Ghee or tikta ghee for oleation (coconut oil if you are vegan). Home-made from organic butter is best. Skip it if you have no gallbladder or have liver or gallbladder issues.',
        'Sesame, sunflower or coconut oil for oil pulling.',
        'Tongue scraper (a spoon with a slightly sharp edge will do, not as well).',
        'Sesame, almond or jojoba oil for abhyanga, or a dosha-specific oil from Banyan.',
        'Mung dal (split yellow mung beans) and basmati rice. Spices: mustard seed, cumin seed, fennel seed, fresh ginger, coriander powder, turmeric.',
        veg, fruit, 'Cilantro, if you like it.',
        'Herbal teas of your choice: tulsi, ginger, mint, or any detox blend. Lemons or limes for your water.',
        'For rasayana: almonds to soak and peel (or blanched almonds), dates, milk of your choice, cinnamon, clove, cardamom, nutmeg.',
    ]
    opt = [
        'Triphala powder or tablets.',
        'Neem tablets (good for excess Pitta and clearing the skin).',
        'Miso with live cultures, for post-fast soup.',
        'Neti pot.',
        'Chyavanprash, or ashwagandha powder or tincture.',
        'Dashamula (powder or chopped herbs) and sesame oil for basti, plus an enema bag.',
        'Epsom salts.',
        'Exfoliating gloves or a soft garshana brush, especially with excess Kapha. A slightly rough towel will do.',
    ]
    return f'''
    <section class="block" id="shopping">
      <h2>Shopping list</h2>
      <h3>You will need</h3>
      {ul(core, 'check')}
      <h3>Optional</h3>
      {ul(opt, 'check')}
      <h3>Where to buy</h3>
      <p>Most Ayurvedic products: {L('https://www.banyanbotanicals.com/', 'Banyan Botanicals')} online (sister company to Dr. Lad’s Ayurveda Institute, rigorously tested for contaminants). Locally, {L('https://pyamandala.com/', 'Prana Yoga and Ayurveda Mandala')} at 33rd and Federal in Denver; call first (303-432-8099). Food from Natural Grocers or similar; for mung dal and spices, {L('https://www.mapquest.com/us/colorado/bombay-bazaar-272463731', 'Bombay Bazaar')}, 3140 S Parker Rd, Aurora. Other herbs: Apothecary Tinctura and other shops around Denver.</p>
    </section>
'''


CARE = f'''
    <section class="block care" id="care">
      <h2>Take care</h2>
      <p>This program is a guide, not medical advice. Fasting and cleansing practices are not right for everyone. If you are pregnant or nursing, take medication, or have diabetes, a history of disordered eating or any other health condition, talk to your doctor before you start. If you feel unwell at any point, eat, rest and <a href="{MAIL}">get in touch</a>.</p>
    </section>
'''


def day_html(d):
    parts = [f'<p class="phase">{d["phase"]}</p>', f'<h2><span>Day {d["num"]}</span> {d["title"]}</h2>']
    if d['note']:
        parts.append(f'<p class="daynote">{d["note"]}</p>')
    if d['jump']:
        parts.append('<p class="jump"><a href="#shopping">Shopping list</a> · <a href="#routine">Daily routine</a> · <a href="#guide">Practice guide</a></p>')
    for name, items in d['sections']:
        if items:
            parts.append(f'<section><h3>{name}</h3>{ul(items)}</section>')
    if d['routine']:
        parts.append('<p class="jump">Plus the <a href="#routine">daily routine</a> and plenty of rest.</p>')
    return f'<article class="day" id="day-{d["num"]}" data-day="{d["num"]}">\n' + '\n'.join('  ' + p for p in parts) + '\n</article>'


def page(slug, season, title, intro, phases, days, before='', routine_start=1):
    nav = ''.join(f'<a href="#day-{d["num"]}" data-day="{d["num"]}" class="ph-{d["phase"].split()[0].lower()}">{d["num"]}</a>' for d in days)
    phase_html = ''.join(f'<li><b>{r}</b> {n}</li>' for r, n in phases)
    html = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} — YogaCybin</title>
  <meta name="description" content="Day-by-day guide for participants of the YogaCybin {title}.">
  <meta name="robots" content="noindex, nofollow">
  <meta name="theme-color" content="#141413">
  <link rel="icon" href="../assets/favicon.png" type="image/png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poiret+One&family=Quicksand:wght@300;400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../styles.css">
  <link rel="stylesheet" href="../cleanse.css">
</head>
<body class="cleanse">
  <a class="skip" href="#days">Skip to the days</a>

  <header class="c-head">
    <a href="../" aria-label="YogaCybin home"><img class="logo" src="../assets/YogaCybin_no_gap_10.svg" alt="YogaCybin" width="145" height="50"></a>
    <h1>{title}</h1>
    <p>{intro}</p>
    <ol class="phases">{phase_html}</ol>
    <p class="toc"><a href="#days">Days</a> · <a href="#routine">Daily routine</a> · <a href="#food">Food</a> · <a href="#shopping">Shopping</a> · <a href="#guide">Practice guide</a></p>
  </header>

  <nav class="daynav" aria-label="Days">{nav}</nav>

  <main>{before}
    <div id="days">
{chr(10).join(day_html(d) for d in days)}
    </div>
    <div class="pager">
      <button type="button" id="prev">← Previous day</button>
      <button type="button" id="all">Show all days</button>
      <button type="button" id="next">Next day →</button>
    </div>
{routine(routine_start)}{food(season)}{shopping(season)}
    <section class="block" id="guide">
      <h2>Practice guide</h2>
      {guides(season)}
    </section>
{CARE}  </main>

  <footer class="footer">
    <p>Questions during the cleanse? <a href="{MAIL}">info@yogacybin.com</a> · <a href="tel:+18888809642">(888) 880-YOGA</a></p>
    <p class="fine">© YogaCybin</p>
  </footer>

  <script src="../cleanse.js"></script>
</body>
</html>
'''
    out = os.path.join(ROOT, slug, 'index.html')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w') as f:
        f.write(html)
    print('wrote', out, len(html))


page('spring-cleanse', 'spring', 'Spring Cleanse',
     'An 18-day Ayurvedic cleanse. Pick your day below; everything you need for it is on one screen.',
     [('1–3', 'Prepare'), ('4–9', 'Cleanse'), ('10–12', 'Deep cleanse'), ('13', 'Break the fast'), ('14–18', 'Rebuild')],
     spring_days(), routine_start=4)

page('fall-cleanse', 'fall', 'Fall Cleanse',
     'A 15-day Ayurvedic cleanse. Pick your day below; everything you need for it is on one screen.',
     [('1–6', 'Ease in'), ('7–9', 'Deep cleanse'), ('10', 'Break the fast'), ('11–15', 'Rebuild')],
     fall_days(), before=FALL_BEFORE)
