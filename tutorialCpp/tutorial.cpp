#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <queue>

struct point{
	char y;
	char x;
	char d;
};

char dx[4] = {0,1,0,-1};
char dy[4] = {1,0,-1,0};

int main() {
	int cases;
	char map[50][51];
	char dist[50][50];
	std::queue<point> q;

	scanf("%d\n", &cases);
	while (cases--) {
		int h, w;
		int i, j;

		scanf("%d %d\n", &h, &w );
		for (i = 0; i < h; i++)
		{
			scanf("%s\n", map[i]);
			for (j = 0; j < w; j++)
				dist[i][j] = 4;
		}

		int result = 0;
		point sp;
		char tile;
		for (i = 0; i < h; i++)
		{
			for (j = 0; j < w; j++)
			{
				if (map[i][j] != '.')
				{
					tile = map[i][j];
					sp.y = i;
					sp.x = j;
					dist[sp.y][sp.x] = 0;

					sp.d = 0;
					q.push(sp);
					sp.d = 1;
					q.push(sp);
					sp.d = 2;
					q.push(sp);
					sp.d = 3;
					q.push(sp);
					while ( !q.empty() )
					{
						point tp;
						char dv;
						tp = q.front();
						q.pop();
						dv = dist[tp.y][tp.x] + 1;
						if (dv > 3)
							continue;

						while (true)
						{
							tp.y += dy[tp.d];
							tp.x += dx[tp.d];
							if (tp.y < 0 || tp.x < 0 || tp.y >= h || tp.x >= w)
								break;

							if (map[tp.y][tp.x] == '.')
							{
								if (dist[tp.y][tp.x] < 4)
									continue;

								dist[tp.y][tp.x] = dv;

								char oldd = tp.d;
								if (oldd % 2 == 0)
								{
									tp.d = 1;
									q.push(tp);
									tp.d = 3;
									q.push(tp);
								}
								else
								{
									tp.d = 0;
									q.push(tp);
									tp.d = 2;
									q.push(tp);
								}
								tp.d = oldd;
							}
							else if (dist[tp.y][tp.x] > 3)
							{
								if (tile == map[tp.y][tp.x])
								{
									result++;
								}
								dist[tp.y][tp.x] = dv;
								break;
							}
						}
					}
				}
			}
		}
		printf("%d\n", result);
	}

	return 0;
}
