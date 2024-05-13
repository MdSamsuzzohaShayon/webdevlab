export function shortDesc(inputString: string, chars: number): string {
  if (inputString.length > chars) {
    return inputString.substring(0, chars) + '...';
  } else {
    return inputString;
  }
}
