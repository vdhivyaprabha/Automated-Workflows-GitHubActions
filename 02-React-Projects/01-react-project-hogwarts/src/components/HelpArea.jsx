import HelpBox from './HelpBox';
import './HelpArea.css';

const HELP_ITEMS = [
  {
    id: 'h1',
    title: 'Gryffindor',
    text: 'Gryffindor values courage, bravery, nerve, and chivalry. Gryffindors mascot is the lion, and its colours are scarlet red and gold (maroon and gold on the ties and scarves)',
  },
  {
    id: 'h1',
    title: 'Hufflepuff',
    text: 'Hufflepuff values hard work, patience, justice, and loyalty. The house mascot is the badger, and canary yellow and black (or golden yellow and graphite in the Fantastic Beasts films) are its colours.',
  },
  {
    id: 'h1',
    title: 'Ravenclaw',
    text: 'Ravenclaw values intelligence, learning, wisdom and wit.The house mascot is an eagle (raven in the Harry Potter and Fantastic Beasts films) and the house colours are blue and bronze (blue and silver in the Harry Potter and Fantastic Beasts films).',
  },{
    id: 'h1',
    title: 'Slytherin',
    text: 'Slytherin values ambition, cunning, leadership, and resourcefulness; the Sorting Hat said in Harry Potter and the Philosopher Stone that Slytherins will do anything to get their way',
  }
];

function HelpArea() {
  return (
    <section data-testid="help-area" id="help-area">
      {HELP_ITEMS.map((item) => (
        <HelpBox key={item.id} title={item.title} text={item.text} />
      ))}
    </section>
  );
}

export default HelpArea;
